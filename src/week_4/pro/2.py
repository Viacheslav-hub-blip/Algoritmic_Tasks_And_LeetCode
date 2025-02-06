import json
def generate_task_report(filename:str):
    with open(filename, 'r') as f:
        file_data  = json.load(f)

        total_tasks  = len(file_data)
        count_completed  = 0
        count_priority = 0

        for task in file_data:
            if task['status'] == 'completed':
                count_completed += 1
            if task['priority'] == 'high':
                count_priority += 1
        return {'total_tasks': total_tasks, 'completed_tasks': count_completed, 'high_priority_tasks': count_priority}


generate_task_report('task.jsonl')
