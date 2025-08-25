# ✈️ Aircraft Damage Classification (Crack vs Dent) & 🖼️ Image Caption Generation  

This repository contains my **Final Project** for the course:  
**“Introduction to Deep Learning & Neural Networks with Keras”**  

The project has **two major components**:  

1. **Aircraft Damage Classification** – A **Convolutional Neural Network (CNN)** with **Transfer Learning (VGG16)** to classify aircraft damages into **Cracks vs. Dents**.  
2. **Image Caption Generation** – Using **BLIP (Bootstrapping Language-Image Pretraining)** to generate meaningful captions for images.  

---

## 📌 Project Overview  

- ✅ Built and trained a CNN for **aircraft damage classification** with **>81% test accuracy**.  
- ✅ Classified **type of damage (Crack / Dent)** instead of just binary damaged vs. normal.  
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

---

## ⚡ How to Run  

1. Clone this repo:  
   ```bash
   git clone https://github.com/your-username/aircraft-damage-and-captioning.git
   cd aircraft-damage-and-captioning

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Download the dataset:
   ```bash
   python download_dataset.py

4. Run the Jupyter notebook:

- Damage_Detection_and_BLIP_Captioning.ipynb

---

## 🚀 Results  

### Aircraft Damage Classification (Crack vs Dent)  
- **Training Accuracy:** ~85%  
- **Test Accuracy:** ~81%  
- **Model Used:** VGG16 (frozen base + fine-tuned dense layers)    

📊 Example:  

| Image | Prediction |
|-------|------------|
| ![crack](sample_images/crack.jpg) | Crack |
| ![dent](sample_images/dent.jpg)   | Dent |

---

### Image Caption Generation (BLIP)  

BLIP generates captions for unseen images:  

- Input: 🖼️ *Aircraft flying in cloudy sky*  
- Output: **"an airplane flying through the clouds"**  

- Input: 🖼️ *Damaged aircraft*  
- Output: **"a damaged airplane parked on the runway"**  

---

## 📜 Certificate  

This project was submitted as part of my completion for **Introduction to Deep Learning & Neural Networks with Keras (IBM)**.  
🎓 Certificate available here → [Add your certificate image/link]  

---

## 🙌 Acknowledgements

- IBM: Introduction to Deep Learning & Neural Networks with Keras
- OpenAI BLIP Model
= Aircraft damage dataset (publicly available)
   
