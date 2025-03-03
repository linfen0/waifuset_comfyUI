import torch
from .waifuset.waifu_scorer import WaifuScorer
import os
import folder_paths
class WaifuScorerNode:
    def __init__(self):
        self.waifu_scorer = None
        self.model_dir = os.path.join(folder_paths.models_dir, "aesthetic")
        
    @classmethod
    def INPUT_TYPES(s):
        # 获取模型目录下的所有safetensors文件
        model_dir = os.path.join(folder_paths.models_dir, "aesthetic")
        model_list = []
        if os.path.exists(model_dir):
            for file in os.listdir(model_dir):
                if file.endswith('.safetensors'):
                    model_list.append(file)
        if not model_list:
            model_list = ["请放入模型文件"]
            
        return {
            "required": {
                "image": ("IMAGE",),
                "model_name": (model_list,),
                "device": (["cuda", "cpu"],),
            },
        }

    RETURN_TYPES = ("FLOAT", "STRING",)
    RETURN_NAMES = ("score", "formatted_score",)
    FUNCTION = "score_image"
    CATEGORY = "image/scoring"

    def score_image(self, image, model_name, device):
        if model_name == "请放入模型文件":
            return (0.0, "Error: No model files found",)
            
        model_path = os.path.join(self.model_dir, model_name)
        
        if self.waifu_scorer is None:
            self.waifu_scorer = WaifuScorer(
                model_path=model_path,
                device=device if device == 'cuda' and torch.cuda.is_available() else 'cpu',
                verbose=True
            )
        elif self.waifu_scorer.model_path != model_path:
            # 如果选择了不同的模型，重新加载
            self.waifu_scorer = WaifuScorer(
                model_path=model_path,
                device=device if device == 'cuda' and torch.cuda.is_available() else 'cpu',
                verbose=True
            )
        
        score = self.waifu_scorer(image)
        formatted_score = f"Aesthetic Score: {score[0]:.2f}"
        
        return (float(score[0]), formatted_score,)

# 更新节点映射
NODE_CLASS_MAPPINGS = {
    "WaifuScorer": WaifuScorerNode,
}

# 更新显示名称映射
NODE_DISPLAY_NAME_MAPPINGS = {
    "WaifuScorer": "Waifu Aesthetic Scorer",
}
