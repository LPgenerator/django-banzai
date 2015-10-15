import hashlib
from datetime import datetime

from lxml import etree

from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files import File

from banzai.models import Package, Attachment

class MailPackage(object):

    def __init__(self, email_from, name_from, subject, message, send_at=None,
                 headers=None, attach_images=u'0', description=u'',
                 attachments=None):
        self.email_from = email_from
        self.name_from = name_from
        self.subject = subject
        self.message = message
        self.send_at = send_at
        self.headers = list() if headers is None else headers
        self.attachments = list() if attachments is None else attachments
        self.attach_images = attach_images
        self.description = description

        self._recipients_data = []
        self._xml = etree.Element('list')
        self._generation_complete = False
        self._package = None

    def add_recipients(self, recipients_list):
        if isinstance(recipients_list, dict):
            recipients_list = [recipients_list]
        for recipient in recipients_list:
            if isinstance(recipient, dict):
                self.add_recipient(
                    recipient['email_to'],
                    recipient.get('name_to', u''),
                    recipient.get('header', {}),
                    recipient.get('fields', {})
                )
            elif isinstance(recipient, (str, unicode)):
                self.add_recipient(recipient)
            else:
                raise RuntimeError('recipients_list must be a dict or string!')

    def add_recipient(self, email_to, name_to=u'', header=None, fields=None):
        header = dict() if header is None else header
        fields = dict() if fields is None else fields
        if self._generation_complete:
            raise RuntimeError('Impossibly add recipient, because '
                               'generation already complete!')
        self._recipients_data.append({
            'email_to': email_to,
            'name_to': name_to,
            'header': header,
            'fields': fields
        })

    def save(self):
        if self._package is None:
            file_name = '{0}#{1}'.format(datetime.now(), settings.SECRET_KEY)
            file_name = hashlib.md5(file_name).hexdigest()
            file_name = '{0}.xml'.format(file_name)

            package_obj = Package(
                emails_all=len(self._recipients_data),
                description=self.description
            )
            xml_content = ContentFile(self.xml_tostring())
            package_obj.file.save(file_name, xml_content)
            package_obj.save()
            for attachment in self.attachments:
                filename = attachment.get_filename()
                fp = open(filename, 'wb+')
                fp.write(attachment.get_payload(decode=True))
                djangofile = File(fp)
                attach = Attachment(name=filename, package=package_obj)
                attach.file.save(filename, djangofile)
                attach.save()
                fp.close()
            self._package = package_obj
        return self._package

    def xml_tostring(self):
        self._generate()
        return etree.tostring(self._xml, encoding='UTF-8',
                              xml_declaration=True)

    def _generate(self):
        if self._generation_complete:
            return
        body_tag = etree.Element('body')

        data_tag = etree.Element('Data')
        data_tag.text = etree.CDATA(self.message)
        body_tag.append(data_tag)
        del data_tag

        email_from_tag = etree.Element('EmailFrom')
        email_from_tag.text = etree.CDATA(self.email_from)
        body_tag.append(email_from_tag)
        del email_from_tag

        name_from_tag = etree.Element('NameFrom')
        name_from_tag.text = etree.CDATA(self.name_from)
        body_tag.append(name_from_tag)
        del name_from_tag

        subject_tag = etree.Element('Subject')
        subject_tag.text = etree.CDATA(self.subject)
        body_tag.append(subject_tag)
        del subject_tag

        attach_images_tag = etree.Element('AttachImages')
        attach_images_tag.text = etree.CDATA(self.attach_images)
        body_tag.append(attach_images_tag)
        del attach_images_tag

        for attach in self.attachments:
            attach_tag = etree.Element(
                'Attach',
                name=attach.get_filename(),
                mimetype=attach.get_content_type()
            )
            attach_tag.text = etree.CDATA(attach.get_payload())
            body_tag.append(attach_tag)
            del attach_tag

        if self.send_at is not None:
            send_at_tag = etree.Element('SendAt')
            send_at_str = self.send_at.strftime('%Y/%m/%d %H:%M')
            send_at_tag.text = etree.CDATA(send_at_str)
            body_tag.append(send_at_tag)
            del send_at_tag, send_at_str

        for header in self.headers:
            header_tag = etree.Element('Header')
            header_tag.attrib['name'] = header['name']
            header_tag.attrib['value'] = header['value']
            body_tag.append(header_tag)
            del header_tag

        self._xml.append(body_tag)
        del body_tag

        users_tag = etree.Element('users')
        for recipient in self._recipients_data:
            current_user_tag = etree.Element('user')

            email_to_tag = etree.Element('EmailTo')
            email_to_tag.text = etree.CDATA(recipient['email_to'])
            current_user_tag.append(email_to_tag)
            del email_to_tag

            if recipient['name_to']:
                name_to_tag = etree.Element('NameTo')
                name_to_tag.text = etree.CDATA(recipient['name_to'])
                current_user_tag.append(name_to_tag)
                del name_to_tag

            if recipient['header']:
                header_tag = etree.Element('Header')
                header_tag.attrib['name'] = recipient['header']['name']
                header_tag.attrib['value'] = recipient['header']['value']
                current_user_tag.append(header_tag)
                del header_tag

            for field in recipient['fields']:
                field_tag = etree.Element(field['name'])
                field_tag.text = etree.CDATA(field['value'])
                current_user_tag.append(field_tag)
                del field_tag

            users_tag.append(current_user_tag)
            del current_user_tag

        self._xml.append(users_tag)
        del users_tag

        self._generation_complete = True
