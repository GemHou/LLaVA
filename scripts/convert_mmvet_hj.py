import json

def convert_json(input_path, output_path):
    with open(input_path, 'r') as input_file:
        data = json.load(input_file)

    new_data = []

    question_id = 1
    for key, value in data.items():
        new_entry = {
            "question_id": question_id,
            "image": value["imagename"],
            "text": value["question"]
        }
        new_data.append(new_entry)
        question_id += 1

    with open(output_path, 'w') as output_file:
        for entry in new_data:
            output_file.write(json.dumps(entry) + '\n')

if __name__ == "__main__":
    input_file_path = "/mnt/nfs/houjing/repo/LLaVA/playground/data/eval/mm-vet/mm-vet.json"
    output_file_path = "/mnt/nfs/houjing/repo/LLaVA/playground/data/eval/mm-vet/llava-mm-vet.jsonl"

    convert_json(input_file_path, output_file_path)
