# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class JobErrorDetails(Model):
    """The Data Lake Analytics job error details.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar error_id: The specific identifier for the type of error encountered
     in the job.
    :vartype error_id: str
    :ivar severity: The severity level of the failure. Possible values
     include: 'Warning', 'Error', 'Info', 'SevereWarning', 'Deprecated',
     'UserWarning'
    :vartype severity: str or
     ~azure.mgmt.datalake.analytics.job.models.SeverityTypes
    :ivar source: The ultimate source of the failure (usually either SYSTEM or
     USER).
    :vartype source: str
    :ivar message: The user friendly error message for the failure.
    :vartype message: str
    :ivar description: The error message description.
    :vartype description: str
    :ivar details: The details of the error message.
    :vartype details: str
    :ivar line_number: The specific line number in the job where the error
     occured.
    :vartype line_number: int
    :ivar start_offset: The start offset in the job where the error was found
    :vartype start_offset: int
    :ivar end_offset: The end offset in the job where the error was found.
    :vartype end_offset: int
    :ivar resolution: The recommended resolution for the failure, if any.
    :vartype resolution: str
    :ivar file_path: The path to any supplemental error files, if any.
    :vartype file_path: str
    :ivar help_link: The link to MSDN or Azure help for this type of error, if
     any.
    :vartype help_link: str
    :ivar internal_diagnostics: The internal diagnostic stack trace if the
     user requesting the job error details has sufficient permissions it will
     be retrieved, otherwise it will be empty.
    :vartype internal_diagnostics: str
    :ivar inner_error: The inner error of this specific job error message, if
     any.
    :vartype inner_error:
     ~azure.mgmt.datalake.analytics.job.models.JobInnerError
    """

    _validation = {
        'error_id': {'readonly': True},
        'severity': {'readonly': True},
        'source': {'readonly': True},
        'message': {'readonly': True},
        'description': {'readonly': True},
        'details': {'readonly': True},
        'line_number': {'readonly': True},
        'start_offset': {'readonly': True},
        'end_offset': {'readonly': True},
        'resolution': {'readonly': True},
        'file_path': {'readonly': True},
        'help_link': {'readonly': True},
        'internal_diagnostics': {'readonly': True},
        'inner_error': {'readonly': True},
    }

    _attribute_map = {
        'error_id': {'key': 'errorId', 'type': 'str'},
        'severity': {'key': 'severity', 'type': 'SeverityTypes'},
        'source': {'key': 'source', 'type': 'str'},
        'message': {'key': 'message', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'details': {'key': 'details', 'type': 'str'},
        'line_number': {'key': 'lineNumber', 'type': 'int'},
        'start_offset': {'key': 'startOffset', 'type': 'int'},
        'end_offset': {'key': 'endOffset', 'type': 'int'},
        'resolution': {'key': 'resolution', 'type': 'str'},
        'file_path': {'key': 'filePath', 'type': 'str'},
        'help_link': {'key': 'helpLink', 'type': 'str'},
        'internal_diagnostics': {'key': 'internalDiagnostics', 'type': 'str'},
        'inner_error': {'key': 'innerError', 'type': 'JobInnerError'},
    }

    def __init__(self, **kwargs):
        super(JobErrorDetails, self).__init__(**kwargs)
        self.error_id = None
        self.severity = None
        self.source = None
        self.message = None
        self.description = None
        self.details = None
        self.line_number = None
        self.start_offset = None
        self.end_offset = None
        self.resolution = None
        self.file_path = None
        self.help_link = None
        self.internal_diagnostics = None
        self.inner_error = None