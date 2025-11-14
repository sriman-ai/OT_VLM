import os
from PIL import Image
from transformers import AutoTokenizer, AutoModelForVision2Seq

input_imgs = r"C:\Users\srima\Desktop\A3_SETS\occupational_safety_\output\video_frames"
out_file = r"C:\Users\srima\Desktop\A3_SETS\occupational_safety_\output\vlm_video_results.txt"
os.makedirs(os.path.dirname(out_file), exist_ok=True)

Q_LIST = [
    "Describe the situation in this frame.",
    "Are there any safety signs or warnings visible?",
    "What unsafe condition or process can you see, if any?",
]

MODEL_NAME = "llava-hf/llava-1.5-7b-hf"

def vlm_qa(image_path, queries, model, tokenizer):
    img = Image.open(image_path).convert("RGB")
    results = []
    for q in queries:
        prompt = f"[INST] {q} [/INST]"
        out = model.generate(inputs={"pixel_values": model.preprocess(img), "input_ids": tokenizer(prompt, return_tensors="pt").input_ids})
        answer = tokenizer.decode(out[0], skip_special_tokens=True)
        results.append((q, answer))
    return results

if __name__ == "__main__":
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForVision2Seq.from_pretrained(MODEL_NAME)

    all_results = []
    for fname in os.listdir(input_imgs):
        if fname.lower().endswith((".jpg", ".png", ".jpeg", ".bmp")):
            fpath = os.path.join(input_imgs, fname)
            anslist = vlm_qa(fpath, Q_LIST, model, tokenizer)
            all_results.append((fname, anslist))
            print(f"Done: {fname}")
    with open(out_file, "w", encoding="utf-8") as f:
        for fname, qas in all_results:
            f.write(f"=== {fname} ===\n")
            for q, a in qas:
                f.write(f"Q: {q}\nA: {a}\n\n")
    print(f"All outputs saved to {out_file}")
