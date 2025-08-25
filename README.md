# ✈️ Aircraft Damage Detection & 🖼️ Image Caption Generation  

This repository contains my **Final Project** for the course:  
**“Introduction to Deep Learning & Neural Networks with Keras”**  

The project has **two major components**:  

1. **Aircraft Damage Detection** – A **Convolutional Neural Network (CNN)** with **Transfer Learning (VGG16)** to classify damaged vs. non-damaged aircraft images.  
2. **Image Caption Generation** – Using **BLIP (Bootstrapping Language-Image Pretraining)** to generate meaningful captions for images.  

---

## 📌 Project Overview  

- ✅ Built and trained a CNN for **aircraft damage classification** with **>81% test accuracy**.  
- ✅ Applied **Transfer Learning (VGG16)** with **data augmentation** and **callbacks** (EarlyStopping, ReduceLROnPlateau).  
- ✅ Implemented **BLIP** for **image captioning** that generates human-like captions.  
- ✅ Explored both **computer vision (classification)** and **vision-language (captioning)** tasks in one project.  

---

## 🛠️ Tech Stack  

- **Frameworks:** TensorFlow, Keras, PyTorch  
- **Models:** CNN, VGG16 (Transfer Learning), BLIP  
- **Languages:** Python  
- **Tools:** Jupyter Notebook, Google Colab  

---

## 📂 Project Structure  

<pre>
  
├──aircraft_damage_dataset_v1/
|  ├── train/
|  │   ├── dent/
|  │   └── crack/
|  ├── valid/
|  │   ├── dent/
|  │   └── crack/
|  └── test/
|      ├── dent/
|      └── crack/ 
├── aircraft_damage_dataset_v1.tar
├── Damage_Detection_and_BLIP_Captioning # BLIP caption generation
├── download_dataset.py                  # Download the dataset
├── requirements.txt                     # Required dependencies
├── .gitignore                           # Avoid venv and dataset
└── README.md                            # Project documentation
  
</pre>
