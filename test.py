import torch
from waifuset.waifu_scorer.predict import WaifuScorer
def test():
    model_path = r"F:\AI_Study_studio\Ai_draw\ComfyUI\models\aesthetic\waifu_scorers_Aesthetic.safetensors"
    #model_repo_or_path = "models/waifu_scorer_v1.0.0"
    images = ["F:\AI_Study_studio\Ai_draw\ComfyUI\output\ComfyUI_rpgmaker_00275_.png"]
    waifu_scorer = WaifuScorer(model_path=model_path, device='cuda' if torch.cuda.is_available() else 'cpu', verbose=True)
    #waifu_scorer.model_name = model_repo_or_path
    return waifu_scorer(images)

if __name__ == "__main__":
    print(test())
