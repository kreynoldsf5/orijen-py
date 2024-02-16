"""Module for Users"""
from uplink import Consumer, Path, Body, json, get, post, put
from orijenpy import helper


@helper.common_decorators
class User(Consumer):
    """Class for Users"""
    def __init__(self, session):
        super().__init__(base_url=session._tenant_url, client=session._session)

    @get('/api/web/custom/namespaces/{namespace}/user_roles')
    def list(self, namespace: Path = 'system'):
        '''List all Users'''

    @json
    @post('/api/web/custom/namespaces/{namespace}/user_roles')
    def create(self, payload: Body, namespace: Path = 'system'):
        '''Create a User'''

    @json
    @post('/api/web/custom/namespaces/{namespace}/users/cascade_delete')
    def delete(self, payload: Body, namespace: Path = 'system'):
        '''Delete a User'''

    @json
    @put('/api/web/custom/namespaces/{namespace}/users/group_add')
    def group(self, payload: Body, namespace: Path = 'system'):
        '''Configure Group(s) for a user'''

    @staticmethod
    def create_payload(
            email: str,
            first_name: str,
            last_name: str,
            group_names: list = [],
            namespace_roles: list = [],
            idm_type: str = 'SSO',
            namespace: str = 'system'
        ):
        """Payload for Create"""
        return {
            "email": email,
            "first_name": first_name,
            "group_names": group_names,
            "idm_type": idm_type,
            "last_name": last_name,
            "name": email,
            "namespace": namespace,
            "namespace_roles": namespace_roles,
            "type": "USER"
        }

    @staticmethod
    def delete_payload(email: str, namespace: str = 'system'):
        """Payload for delete"""
        return {
            "email": email,
            "namespace": namespace
        }

    @staticmethod
    def group_payload(user: str, group_names: list):
        """Payload for group"""
        return {
            "group_names": group_names,
            "username": user
        }