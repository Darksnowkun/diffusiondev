from diffusers import StableDiffusionPipeline
import torch
import os
from dotenv import load_dotenv

from diffusers.pipelines.stable_diffusion import safety_checker
def sc(self, clip_input, images) : return images, [False for i in images]
# edit the StableDiffusionSafetyChecker class so that, when called, it just returns the images and an array of True values
safety_checker.StableDiffusionSafetyChecker.forward = sc

def setup():
    load_dotenv()
    token=os.getenv('HUG_TOKEN')
    return token

print(setup())

url = "abyssorangemix3AOM3_aom3a1.safetensors"
pipeline = StableDiffusionPipeline.from_single_file(url)
from diffusers.pipelines.stable_diffusion import safety_checker
def sc(self, clip_input, images) : return images, [False for i in images]
# edit the StableDiffusionSafetyChecker class so that, when called, it just returns the images and an array of True values
safety_checker.StableDiffusionSafetyChecker.forward = sc

# Prompts
my_prompt = "sfw, space, floating, stars, sun, moon, lunar, supernova, sfw"
image = pipeline(prompt=my_prompt, num_inference_steps=10).images[0]
from diffusers.pipelines.stable_diffusion import safety_checker
def sc(self, clip_input, images) : return images, [False for i in images]
# edit the StableDiffusionSafetyChecker class so that, when called, it just returns the images and an array of True values
safety_checker.StableDiffusionSafetyChecker.forward = sc
image.save("test13.png")
image