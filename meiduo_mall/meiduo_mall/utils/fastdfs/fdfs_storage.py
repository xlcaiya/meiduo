from django.conf import settings
from django.core.files.storage import Storage
from fdfs_client.client import Fdfs_client


class FastDFSStorage(Storage):
    def __init__(self, base_url=None, client_conf=None):
        """

        :param base_url:用户构建图片完整路径
        :param client_conf: FastDFS的配置文件路径
        """
        if not base_url:
            base_url = settings.FDFS_URL
        self.base_url = base_url
        if not client_conf:
            client_conf = settings.FDFS_CLIENT_CONF
        self.client_conf = client_conf

    def _open(self, name, mode='rb'):
        """
        用不到打开文件, 所以省略
        :param name:
        :param mode:
        :return:
        """
        pass

    def _save(self, name, content):
        """
        在FastDFS中保存文件
        :param name: 传入的文件名
        :param content: 文件内容
        :return: 保存到数据库的FastDFS的文件名
        """
        print('name: %s' % name)
        print('content: %s' % content)
        client = Fdfs_client(self.client_conf)
        print('client: %s' % client)
        ret = client.upload_by_buffer(content.read())
        print('ret: %s' % ret)
        print('content: %s' % content)
        if ret.get('Status') != 'Upload successed.':
            raise Exception('文件不存在')
        file_name = ret.get('Remote file_id')
        return file_name

    def url(self, name):
        """
        返回文件的完整URL路径
        :param name: 数据库中保存的文件名
        :return: 完整的URL
        """
        return self.base_url + name

    def exists(self, name):
        """
        判断文件是否存在, FastDFS可以自行解决文件的重名问题
        所以此处返回False, 告诉Django上传的都是新文件
        :param name: 文件名
        :return: False
        """
        return False
