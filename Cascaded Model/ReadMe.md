
# Cascaded Model Architecture and Implementation:

## Architecture

<p align="center">
    <img src="https://github.com/zeeshannisar/Research-Paper-Contribution/blob/master/ReadMe%20Images/Architecture.png" >
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






