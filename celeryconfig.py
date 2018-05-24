broker_url = 'amqp://'
result_backend = 'rpc://'
task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
enable_utc = True
task_annotations = {
    'tasks.reverse_string': {'rate_limit': '10/m'}
}
task_routes = {
    'tasks.reverse_string': 'low-priority',
}

