# Fruit_recognizer

An image classification model from data collection, cleaning, model training, deployment and API integration. <br/>
The model can classify 20 different types of fruits <br/>
The types are following: <br/>

1. Mangoes
2. Apples
3. Pineapples
4. Oranges
5. Papaya
6. Watermelon
7. Muskmelon
8. Blackberry
9. Litchi
10. Grapes
11. Kiwi
12. Plums
13. Peaches
14. Strawberries
15. Tomato
16. Cherry
17. Bael
18. Cucumber
19. Mulberry
20. Ice Apple

# Dataset Preparation

**Data Collection:** Downloaded from DuckDuckGo using term name <br/>
**DataLoader:** Used fastai DataBlock API to set up the DataLoader. <br/>
**Data Augmentation:** fastai provides default data augmentation which operates in GPU. <br/>
Details can be found in `notebooks/data_prep.ipynb`

# Training and Data Cleaning

**Training:** Fine-tuned a resnet34 model for 5 epochs (2 times) and got upto ~85% accuracy. <br/>
**Data Cleaning:** This part took the highest time. Since I collected data from browser, there were many noises. Also, there were images that contained. I cleaned and updated data using fastai ImageClassifierCleaner. I cleaned the data each time after training or finetuning, except for the last time which was the final iteration of the model. <br/>

# Model Deployment

I deployed to model to HuggingFace Spaces Gradio App. The implementation can be found in `deployment` folder or [here](https://huggingface.co/spaces/sakibice007/Fruits_recognization). <br/>
<img src = "deployment\Screenshot_1.jpg" width="700" height="350">

# API integration with GitHub Pages

The deployed model API is integrated [here](https://sakibhasanice.github.io/Fruit_recognizer/) in GitHub Pages Website. Implementation and other details can be found in `docs` folder.
