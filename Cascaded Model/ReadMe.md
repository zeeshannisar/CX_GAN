# Cascaded Model:
In our Cascaded Model we aim to acheive two cascaded objectives:
  +  Learning to generate counterfactual instances (CIs)
  +  Learning to produce a counterfactual explanation (CX) w.r.t. the generated CI.
  
We view CI generation as unpaired image-to-image translation and CX as image-to-image conversion mapping. We represent the input domain as `X`, consisting of `N` images and the counterfactual domain as `Y` comprised of `M` images. For CI generation, we aim to learn a mapping function such that the distribution of generated images `G(X)` closely matches with input images `X`, and becomes indistinguishable from the distribution of images in `Y`. To impose this constraint, we pose CI generation as an unpaired image-to-image translation problem and adopt [CycleGAN: Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networks](https://arxiv.org/abs/1703.10593) to learn the model. The trained model is then fed with input image x<sub>i</sub> in order to generate CI as y<sub>i</sub>. As a result, we obtain input-counterfactual image pairs (x<sub>i</sub> ; y<sub>i</sub>) for subsequent `CX`. Following [VA-GAN: Visual Feature Attribution using Wasserstein GANs](https://arxiv.org/abs/1711.08998), we define CX as a map `M(x)` that, when added into input image x<sub>i</sub> produce counterfactual image y<sub>i</sub> via:
<p align="center">
  <b> y<sub>i</sub> = x<sub>i</sub> + M(x<sub>i</sub>) </b>
</p>

## Architecture

<p align="center">
    <img src="https://github.com/zeeshannisar/CX_GAN/blob/master/ReadMe%20Images/cascaded%20model.png" >
</p>

## Implementation and Results:

#### Synthetic Data
The entire experiments and evaluations for Synthetic data had carried out for a synthetically generated dataset. The script to generate synthetic data can be found at [Synthetic Data Generate Script](https://github.com/zeeshannisar/Research-Paper-Contribution/blob/master/Cascaded%20Model/Synthetic%20Data/implementation/Script%20to%20Prepare%20Synthetic%20Data.ipynb) originally 
inspired from [VA-GAN](https://arxiv.org/abs/1711.08998). We have used [CycleGAN](https://arxiv.org/abs/1703.10593) as our [Step-1](https://github.com/zeeshannisar/Research-Paper-Contribution/blob/master/Cascaded%20Model/Synthetic%20Data/implementation/Step%201-Generate%20Normal%20Distribution%20from%20Infected%20Distribution%20with%20CycleGANs.ipynb) for CI generation. [Step-1](https://github.com/zeeshannisar/Research-Paper-Contribution/blob/master/Cascaded%20Model/Synthetic%20Data/implementation/Step%201-Generate%20Normal%20Distribution%20from%20Infected%20Distribution%20with%20CycleGANs.ipynb) is used to generate input-counterfactual image pairs. The results of the [Step-1](https://github.com/zeeshannisar/Research-Paper-Contribution/blob/master/Cascaded%20Model/Synthetic%20Data/implementation/Step%201-Generate%20Normal%20Distribution%20from%20Infected%20Distribution%20with%20CycleGANs.ipynb) seems like below.

<p align="center">
    <img src="https://github.com/zeeshannisar/Research-Paper-Contribution/blob/master/Cascaded%20Model/Synthetic%20Data/outputs/Step%201.png" >
</p>

Following [VA-GAN](https://arxiv.org/abs/1711.08998), we define CX as [Step-2](https://github.com/zeeshannisar/Research-Paper-Contribution/blob/master/Cascaded%20Model/Synthetic%20Data/implementation/Step%202-Proposed%20approach%20to%20detect%20infectious%20Regions.ipynb) as a map `M(x)` that is when added to input image x<sub>i</sub> produce counterfactual image y<sub>i</sub>. In addition to a map `M(x)` we have also generate heatmaps for a better visualization.

<p align="center">
    <img src="https://github.com/zeeshannisar/Research-Paper-Contribution/blob/master/Cascaded%20Model/Synthetic%20Data/outputs/Step%202.png" >
</p>

#### BRATS Data

The entire experiments and evaluations for BRATS data had carried out on BRATS 2017 dataset.We have used [CycleGAN](https://arxiv.org/abs/1703.10593) as our [Base-Network/Step-1](https://github.com/zeeshannisar/Research-Paper-Contribution/blob/master/Cascaded%20Model/BRATS%20Data/implementation/Step%201-Generate%20Normal%20Distribution%20from%20Infected%20Distribution%20with%20CycleGANs.ipynb) for CI generation. [Step-1](https://github.com/zeeshannisar/Research-Paper-Contribution/blob/master/Cascaded%20Model/BRATS%20Data/implementation/Step%201-Generate%20Normal%20Distribution%20from%20Infected%20Distribution%20with%20CycleGANs.ipynb) is used to generate input-counterfactual image pairs. The results of the [Step-1](https://github.com/zeeshannisar/Research-Paper-Contribution/blob/master/Cascaded%20Model/BRATS%20Data/implementation/Step%201-Generate%20Normal%20Distribution%20from%20Infected%20Distribution%20with%20CycleGANs.ipynb) seems like below.

<p align="center">
    <img src="https://github.com/zeeshannisar/Reseacrh-Paper-Contribution/blob/master/Cascaded%20Model/BRATS%20Data/outputs/output-step%231.png" >
</p>

Following [VA-GAN](https://arxiv.org/abs/1711.08998), we define CX as [Step-2](https://github.com/zeeshannisar/Research-Paper-Contribution/blob/master/Cascaded%20Model/BRATS%20Data/implementation/Step%202-Proposed%20approach%20to%20detect%20infectious%20Regions.ipynb) as a map `M(x)` that is when added to input image x<sub>i</sub> produce counterfactual image y<sub>i</sub>. In addition to a map `M(x)` we have also generated heatmaps for a better visualization.

<p align="center">
    <img src="https://github.com/zeeshannisar/Reseacrh-Paper-Contribution/blob/master/Cascaded%20Model/BRATS%20Data/outputs/output-step%232.png" >
</p>






