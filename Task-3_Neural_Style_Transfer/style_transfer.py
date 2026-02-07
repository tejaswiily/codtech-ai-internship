import torch
import torch.nn as nn
import torch.optim as optim
from PIL import Image
import torchvision.transforms as transforms
import torchvision.models as models
def load_image(path, max_size=512):
    image = Image.open(path).convert('RGB')
    transform = transforms.Compose([
        transforms.Resize((max_size, max_size)),
        transforms.ToTensor()
    ])
    return transform(image).unsqueeze(0)
def run_style_transfer(content_path, style_path):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    content = load_image(content_path).to(device)
    style = load_image(style_path).to(device)
    model = models.vgg19(weights=models.VGG19_Weights.DEFAULT).features.to(device).eval()
    target = content.clone().requires_grad_(True)
    optimizer = optim.Adam([target], lr=0.02)
    mse = nn.MSELoss()
    for step in range(300):
        target_features = model(target)
        content_features = model(content)
        style_features = model(style)
        loss = mse(target_features, content_features) + mse(target_features, style_features)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        if step % 50 == 0:
            print("Step:", step, "Loss:", loss.item())
    output = target.cpu().clone().squeeze(0)
    output = transforms.ToPILImage()(output)
    output.save("output.jpg")
    print("Saved output.jpg")
def main():
    print("=== Neural Style Transfer ===")
    content_path = input("Enter path to content image: ")
    style_path = input("Enter path to style image: ")
    run_style_transfer(content_path, style_path)
if __name__ == "__main__":
    main()