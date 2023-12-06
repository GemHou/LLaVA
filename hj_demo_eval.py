from llava.model.builder import load_pretrained_model
from llava.mm_utils import get_model_name_from_path
from llava.eval.run_llava import eval_model

model_path = "/mnt/nfs/houjing/model_weights/llava-v1.5-7b"  # /home/zhangqi1/nfs/zhangqi/zhangqi_nfs/DLM-project/public_models/modelWeights/vicuna-13b-v1.5
prompt = "What is in the picture and which one is more cute?"  # What are the things I should be cautious about when I visit here?
image_file = "/mnt/nfs/houjing/repo/LLaVA/fig/20231206-105333.jpg"  # https://llava-vl.github.io/static/images/view.jpg


args = type('Args', (), {
    "model_path": model_path,
    "model_base": None,
    "model_name": get_model_name_from_path(model_path),
    "query": prompt,
    "conv_mode": None,
    "image_file": image_file,
    "sep": ",",
    "temperature": 0,
    "top_p": None,
    "num_beams": 1,
    "max_new_tokens": 512
})()

print("prompt: ", prompt)
print("answer: ", end="")
eval_model(args)
