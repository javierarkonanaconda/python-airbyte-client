from com.arkondata.airbyte.client import ApiException
from com.arkondata.airbyte.client.api.jobs_api import JobsApi
from com.arkondata.airbyte.client.model.job_id_request_body import JobIdRequestBody


class Job:
    def __init__(self, jobs_api_instance: JobsApi):
        if jobs_api_instance is not None:
            self.jobs_api_instance = jobs_api_instance
        else:
            raise Exception("error on destination_definition_api")

    def get_job_debug_info(self, job_id):
        job_id_request_body = JobIdRequestBody(
            id=job_id,
        )
        try:
            api_response = self.jobs_api_instance.get_job_debug_info(job_id_request_body)
            return api_response
        except ApiException as e:
            print("Exception when calling JobsApi->get_job_debug_info: %s\n" % e)
