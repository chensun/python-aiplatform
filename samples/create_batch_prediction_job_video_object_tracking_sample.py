# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START aiplatform_create_batch_prediction_job_video_object_tracking_sample]
from google.cloud import aiplatform
from google.protobuf import json_format
from google.protobuf.struct_pb2 import Value


def create_batch_prediction_job_video_object_tracking_sample(
    display_name: str,
    model_name: str,
    gcs_source_uri: str,
    gcs_destination_output_uri_prefix: str,
    project: str,
):
    client_options = dict(api_endpoint="us-central1-aiplatform.googleapis.com")
    client = aiplatform.JobServiceClient(client_options=client_options)
    location = "us-central1"
    parent = "projects/{project}/locations/{location}".format(
        project=project, location=location
    )
    model_parameters_dict = {"confidenceThreshold": 0.0}
    model_parameters = json_format.ParseDict(model_parameters_dict, Value())

    batch_prediction_job = {
        "display_name": display_name,
        # Format: 'projects/{project}/locations/{location}/models/{model_id}'
        "model": model_name,
        "model_parameters": model_parameters,
        "input_config": {
            "instances_format": "jsonl",
            "gcs_source": {"uris": [gcs_source_uri]},
        },
        "output_config": {
            "predictions_format": "csv",
            "gcs_destination": {"output_uri_prefix": gcs_destination_output_uri_prefix},
        },
    }
    response = client.create_batch_prediction_job(
        parent=parent, batch_prediction_job=batch_prediction_job
    )
    print("response")
    print(" name:", response.name)
    print(" display_name:", response.display_name)
    print(" model:", response.model)
    print(
        " model_parameters:", json_format.MessageToDict(response._pb.model_parameters)
    )
    print(" generate_explanation:", response.generate_explanation)
    print(" state:", response.state)
    print(" create_time:", response.create_time)
    print(" start_time:", response.start_time)
    print(" end_time:", response.end_time)
    print(" update_time:", response.update_time)
    print(" labels:", response.labels)
    input_config = response.input_config
    print(" input_config")
    print("  instances_format:", input_config.instances_format)
    gcs_source = input_config.gcs_source
    print("  gcs_source")
    print("   uris:", gcs_source.uris)
    bigquery_source = input_config.bigquery_source
    print("  bigquery_source")
    print("   input_uri:", bigquery_source.input_uri)
    output_config = response.output_config
    print(" output_config")
    print("  predictions_format:", output_config.predictions_format)
    gcs_destination = output_config.gcs_destination
    print("  gcs_destination")
    print("   output_uri_prefix:", gcs_destination.output_uri_prefix)
    bigquery_destination = output_config.bigquery_destination
    print("  bigquery_destination")
    print("   output_uri:", bigquery_destination.output_uri)
    dedicated_resources = response.dedicated_resources
    print(" dedicated_resources")
    print("  starting_replica_count:", dedicated_resources.starting_replica_count)
    print("  max_replica_count:", dedicated_resources.max_replica_count)
    machine_spec = dedicated_resources.machine_spec
    print("  machine_spec")
    print("   machine_type:", machine_spec.machine_type)
    print("   accelerator_type:", machine_spec.accelerator_type)
    print("   accelerator_count:", machine_spec.accelerator_count)
    manual_batch_tuning_parameters = response.manual_batch_tuning_parameters
    print(" manual_batch_tuning_parameters")
    print("  batch_size:", manual_batch_tuning_parameters.batch_size)
    output_info = response.output_info
    print(" output_info")
    print("  gcs_output_directory:", output_info.gcs_output_directory)
    print("  bigquery_output_dataset:", output_info.bigquery_output_dataset)
    error = response.error
    print(" error")
    print("  code:", error.code)
    print("  message:", error.message)
    details = error.details
    partial_failures = response.partial_failures
    for partial_failure in partial_failures:
        print(" partial_failure")
        print("  code:", partial_failure.code)
        print("  message:", partial_failure.message)
        details = partial_failure.details
    resources_consumed = response.resources_consumed
    print(" resources_consumed")
    print("  replica_hours:", resources_consumed.replica_hours)
    completion_stats = response.completion_stats
    print(" completion_stats")
    print("  successful_count:", completion_stats.successful_count)
    print("  failed_count:", completion_stats.failed_count)
    print("  incomplete_count:", completion_stats.incomplete_count)


# [END aiplatform_create_batch_prediction_job_video_object_tracking_sample]