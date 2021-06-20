# Counterfactual Explanation and Instance-Generation using Cycle-Consistent Generative Adversarial Networks
This Repository contains the code of our submitted paper titled **Counterfactual Explanation and Instance-Generation using Cycle-Consistent Generative Adversarial Networks** at [Information Fusion](https://www.sciencedirect.com/journal/information-fusion). In this paper, we present two separate methods to address the counterfactual explanations (CX). A counterfactual explanation (CX) explicates a casual reasoning process of the form: “if X had not happened, then Y would not have happened”. However, existing CX approaches [[CAM](https://arxiv.org/abs/1512.04150), [Grad-CAM](https://arxiv.org/abs/1610.02391)] are deficient at supplementing counterfactual explanations with plausible counterfactual instances (CIs). To address the issue, we develop a novel CX/CI generation method in which we view CI generation as unpaired imageto-image translation and CX as image-to-image conversion mapping. The method is built on generative adversarial networks (GANs) with a cyclically-consistent loss function. Initially, we develop a [Cascaded Model](#cascaded-model) to learn CX and CI generation individually. Then, we develop an [Integrated End-to-End Model](##integrated-end-to-end-model) for joint learning of both CX and CI. We evaluate our proposed method on three different datasets: [Synthetic](#synthetic-data), [Tuberculosis](#Tuberculosis-chest-x-ray-data) and [BraTS](#brats-data). All experiments confirm the efficacy of the proposed method in generating accurate CX and CI.

## Proposed Models and Results
  + [Cascaded Model](#cascaded-model)
  + [Integrated End-to-End Model](#integrated-end-to-end-model)
  + [Results](#results)
  
### Cascaded Model:
In our Cascaded Model we aim to acheive two cascaded objectives:
  +  Learning to generate CIs
  +  Learning to produce a CX w.r.t. the generated CI.
  
We view CI generation as unpaired image-to-image translation and CX as image-to-image conversion mapping. We represent the input domain as `X`, consisting of `N` images and the counterfactual domain as `Y` comprised of `M` images. For CI generation, we aim to learn a mapping function such that the distribution of generated images `G(X)` closely matches with input images `X`, and becomes indistinguishable from the distribution of images in `Y`. To impose this constraint, we pose CI generation as an unpaired image-to-image translation problem and adopt [CycleGAN:Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks](https://arxiv.org/abs/1703.10593) to learn the model. The trained model is then fed with input image x<sub>i</sub> in order to generate CI as y<sub>i</sub>. As a result, we obtain input-counterfactual image pairs (x<sub>i</sub> ; y<sub>i</sub>) for subsequent `CX`. Following [Visual Feature Attribution using Wasserstein GANs](https://arxiv.org/abs/1711.08998), we define CX as a map `M(x)` that, when added into input image x<sub>i</sub> produce counterfactual image y<sub>i</sub> via:
<p align="center">
  <b> y<sub>i</sub> = x<sub>i</sub> + M(x<sub>i</sub>) </b>
</p>

#### Cascaded Model Architecture:

<p align="center">
    <img src="https://github.com/zeeshannisar/CX_GAN/blob/master/ReadMe%20Images/cascaded%20model.png" >
</p>

## Implementation and Results:

#### Synthetic Data
The entire experiments and evaluations for Synthetic data had carried out for a synthetically generated dataset. The script to generate synthetic data can be found at [Synthetic Data Generate Script](https://github.com/zeeshannisar/Research-Paper-Contribution/blob/master/Cascaded%20Model/Synthetic%20Data/implementation/Script%20to%20Prepare%20Synthetic%20Data.ipynb) originally 
inspired from [**Visual Feature Attribution using Wasserstein GANs**](https://arxiv.org/abs/1711.08998). We have used [**CycleGAN:Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks**](https://arxiv.org/abs/1703.10593) as our [Base-Network/Step-1](https://github.com/zeeshannisar/Research-Paper-Contribution/blob/master/Cascaded%20Model/Synthetic%20Data/implementation/Step%201-Generate%20Normal%20Distribution%20from%20Infected%20Distribution%20with%20CycleGANs.ipynb) to generate a normal distribution against an anomalous distribution. [Step-1](https://github.com/zeeshannisar/Research-Paper-Contribution/blob/master/Cascaded%20Model/Synthetic%20Data/implementation/Step%201-Generate%20Normal%20Distribution%20from%20Infected%20Distribution%20with%20CycleGANs.ipynb) is used for generating pairs i.e., for each anomalous image we get a normal image. The results of the [Step-1](https://github.com/zeeshannisar/Research-Paper-Contribution/blob/master/Cascaded%20Model/Synthetic%20Data/implementation/Step%201-Generate%20Normal%20Distribution%20from%20Infected%20Distribution%20with%20CycleGANs.ipynb) seems like below.

<p align="center">
    <img src="https://github.com/zeeshannisar/Research-Paper-Contribution/blob/master/Cascaded%20Model/Synthetic%20Data/outputs/Step%201.png" >
</p>

Finally we have introduced an approach as [Step-2](https://github.com/zeeshannisar/Research-Paper-Contribution/blob/master/Cascaded%20Model/Synthetic%20Data/implementation/Step%202-Proposed%20approach%20to%20detect%20infectious%20Regions.ipynb) to detect the infectious region using the concept of **what mask M(x) added to x changes it to y** as stated in [**Visual Feature Attribution using Wasserstein GANs**](https://arxiv.org/abs/1711.08998). In addition to masks we have also generate heatmaps for a better visualization.

<p align="center">
    <img src="https://github.com/zeeshannisar/Research-Paper-Contribution/blob/master/Cascaded%20Model/Synthetic%20Data/outputs/Step%202.png" >
</p>

#### BRATS Data

The entire experiments and evaluations for BRATS data had carried out on BRATS 2017 dataset. We have used
[**CycleGAN:Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks**](https://arxiv.org/abs/1703.10593) as our
[Base-Network/Step-1](https://github.com/zeeshannisar/Research-Paper-Contribution/blob/master/Cascaded%20Model/BRATS%20Data/implementation/Step%201-Generate%20Normal%20Distribution%20from%20Infected%20Distribution%20with%20CycleGANs.ipynb) to generate a normal distribution against an anomalous distribution. [Step-1](https://github.com/zeeshannisar/Research-Paper-Contribution/blob/master/Cascaded%20Model/BRATS%20Data/implementation/Step%201-Generate%20Normal%20Distribution%20from%20Infected%20Distribution%20with%20CycleGANs.ipynb) is used for generating pairs i.e., for each anomalous image we get a normal image. The results of the [Step-1](https://github.com/zeeshannisar/Research-Paper-Contribution/blob/master/Cascaded%20Model/BRATS%20Data/implementation/Step%201-Generate%20Normal%20Distribution%20from%20Infected%20Distribution%20with%20CycleGANs.ipynb) seems like below.

<p align="center">
    <img src="https://github.com/zeeshannisar/Reseacrh-Paper-Contribution/blob/master/Cascaded%20Model/BRATS%20Data/outputs/output-step%231.png" >
</p>

Finally we have introduced an approach as [Step-2](https://github.com/zeeshannisar/Research-Paper-Contribution/blob/master/Cascaded%20Model/BRATS%20Data/implementation/Step%202-Proposed%20approach%20to%20detect%20infectious%20Regions.ipynb) to detect the infectious region using the concept of **what mask M(x) added to x changes it to y** as stated in [**Visual Feature Attribution using Wasserstein GANs**](https://arxiv.org/abs/1711.08998). In addition to masks we have also generate heatmaps for a better visualization.

<p align="center">
    <img src="https://github.com/zeeshannisar/Reseacrh-Paper-Contribution/blob/master/Cascaded%20Model/BRATS%20Data/outputs/output-step%232.png" >
</p>

### Integrated End-to-End Model:
A disadvantage of the cascaded model is that separate networks are trained for CX and CI generation, and the performance of CX network relies on efficacy of the CI generation network. This section presents a method for joint learning of both CX and CI through an integrated model. We built on [CycleGAN:Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks](https://arxiv.org/abs/1703.10593) by empowering it to describe transformations while generating pairs across domains. In contrast to the standard CycleGAN, where G and F directly map samples from one domain to another, we want G or F to learn changes that can be made in images of one domain in order to produce images of another domain.

#### Integrated Model Architecture:

<p align="center">
    <img src="https://github.com/zeeshannisar/CX_GAN/blob/master/ReadMe%20Images/integrated%20model.png" >
</p>
  
### Results:
We perform experiments on a synthetic dataset and two publically available medical imaging datasets including BraTS and tuberculosis datasets (i.e. Shenzhen, Montgomery County and Korean Institute of Tuberculosis). We evaluate our proposed method against comparable visual explanation methods including [CAM](https://arxiv.org/abs/1512.04150), [Grad-CAM](https://arxiv.org/abs/1610.02391) and [VA-GAN](https://arxiv.org/abs/1711.08998), where [CAM](https://arxiv.org/abs/1512.04150) and [Grad-CAM](https://arxiv.org/abs/1610.02391) use classification networks, while [VA-GAN](https://arxiv.org/abs/1711.08998) and the proposed CXGAN employ image translation networks.

#### Synthetic Data:
In addition to real medical imaging datasets, we evaluate both the proposed and related methods on a synthetically generated dataset of 10000 128x128 images classified into two classes. One half of the dataset represents a healthy control group (label 0) and another half represents a patient group (label 1). The dataset is generated by close adherence to the data generation process set out in [VA-GAN](https://arxiv.org/abs/1711.08998).
<p align="center">
    <img src="https://github.com/zeeshannisar/CX_GAN/blob/master/ReadMe%20Images/synthetic.png" >
</p>

#### Tuberculosis chest X-ray Data:
This dataset contains de-identified Chest X-Rays (CXRs) from three different public resources: **(1)** the National Institute of Health (NIH) Tuberculosis Chest X-ray database, **(2)** the Belarus Tuberculosis database, and **(3)** Korean Institute of Tuberculosis (KIT) under Korean National Tuberculosis Association, South Korea. The NIH is further categorized into two separate datasets: (a) Montgomery County (MC) and (b) Shenzhen. The Montgomery and Shenzhen dataset contains 138 and 662 patients respectively, with and without TB. The MC Dataset consists of 138 CXRs including 80 normal (i.e., without TB) and 58 anomalous (i.e., with TB) CXRs. The Shenzhen dataset comprises of 662 CXRs where 326 are normal, and 336 are anomalous CXRs. The Belarus dataset has a total of 304 CXRs of patients with anomalous CXRs. The KIT dataset contains 10, 848 DICOM images with 7,020 normal and 3,828 anomalous CXRs.  Following the experimental setup of [4], the experimental evaluation is performed on Shenzhen and MC Dataset by acquiring pixel-level labels from the authors of [4] to evaluate the performance of our proposed approach.

The input data is preprocessed with the following steps: (1) border from the edges of each CXR is cropped to exempt noisy ratio, (2) from 4K×4K pixels, each CXR is resized to 527×527 pixels and cropped 15 pixels away randomly to retain lesions shape in abnormal regions. Any additional augmentations (except for horizontal mirroring and flipping) allowable for lesion deformation is not adopted. In the final step, each data sample is normalized with z-score normalization. We split the overall dataset to 80:20 for training and validation/test set.
<p align="center">
    <img src="https://github.com/zeeshannisar/CX_GAN/blob/master/ReadMe%20Images/TB.png" >
</p>

#### BraTS Data:
The dataset contains brain MRIs classified into normal and tumorous classes. We preprocess the data to filter-out MRI slices that contain the full brain. The dataset contains 3174 images where 2711 are tumorous and 463 non-tumorous. We split each set into 80-20 train/test sets, resulting in 2538 training images and 636 testing images. The filtered slices are resized to 256 * 256 and the
data normalized to the 0-to-1 range. We further increase the data size by performing run-time augmentation on training
sets through random jittering and mirroring. For augmenting, the images are scaled to 286 * 286 and then randomly
cropped to 256 * 256.
<p align="center">
    <img src="https://github.com/zeeshannisar/CX_GAN/blob/master/ReadMe%20Images/BRATS.png" >
</p>



