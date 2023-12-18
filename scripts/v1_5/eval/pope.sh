#!/bin/bash

python -m llava.eval.model_vqa_loader \
    --model-path /mnt/nfs/houjing/model_weights/llava-v1.5-7b \
    --question-file /mnt/nfs/houjing/repo/LLaVA/playground/data/eval/pope/lava_pope_test.jsonl \
    --image-folder ./playground/data/eval/pope/val2014 \
    --answers-file ./playground/data/eval/pope/answers/llava-v1.5-7b.jsonl \
    --temperature 0 \
    --conv-mode vicuna_v1

python llava/eval/eval_pope.py \
    --annotation-dir ./playground/data/eval/pope/coco \
    --question-file /mnt/nfs/houjing/repo/LLaVA/playground/data/eval/pope/lava_pope_test.jsonl \
    --result-file ./playground/data/eval/pope/answers/llava-v1.5-7b.jsonl
