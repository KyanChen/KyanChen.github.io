
# 📝 Publications

<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/H-SRDC.png"><img src='image/H-SRDC.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>Towards Uncovering the Intrinsic Data Structures for Unsupervised Domain Adaptation using Structurally Regularized Deep Clustering</b><br>
<i>IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI), 2022</i><br>
<b>Hui Tang</b>, Xiatian Zhu, Ke Chen, Kui Jia, and CL Philip Chen<br>
[<a href="https://arxiv.org/pdf/2012.04280">PDF</a>] [<a href="https://github.com/huitangtang/H-SRDC">Code</a>] [<a href="https://huitangtang.github.io/H-SRDC/">Page</a>]<br>
<div style="text-align: justify">
We are motivated by a Unsupervised domain adaptation (UDA) assumption of structural similarity across domains, 
and propose to directly uncover the intrinsic target discrimination via constrained clustering, 
where we constrain the clustering solutions using structural source regularization that hinges on the very same assumption. 
Technically, we propose a hybrid model of Structurally Regularized Deep Clustering, 
which integrates the regularized discriminative clustering of target data with a generative one, 
and we thus term our method as H-SRDC.
</div>
</div>

</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/DisClusterDA.png"><img src='image/DisClusterDA.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>Unsupervised domain adaptation via distilled discriminative clustering</b><br>
<i>Pattern Recognition, 2022</i><br>
<b>Hui Tang</b>, Yaowei Wang, and Kui Jia<br>
[<a href="https://arxiv.org/pdf/2302.11984">PDF</a>] [<a href="https://github.com/huitangtang/DisClusterDA">Code</a>] [<a href="https://kyanchen.github.io/DisClusterDA/">Page</a>]<br>
<div style="text-align: justify">
Motivated by the fundamental assumption for domain adaptability, we re-cast the domain adaptation problem as discriminative clustering of target data, 
given strong privileged information provided by the closely related, labeled source data. 
Technically, we use clustering objectives based on a robust variant of entropy minimization that adaptively filters target data, 
a soft Fisher-like criterion, and additionally the cluster ordering via centroid classification. 
To distill discriminative source information for target clustering, we propose to jointly train the network using parallel, supervised learning objectives over labeled source data. 
</div>
</div>

</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/ViCatDA.png"><img src='image/ViCatDA.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>Vicinal and categorical domain adaptation</b><br>
<i>Pattern Recognition, 2021</i><br>
<b>Hui Tang</b> and Kui Jia<br>
[<a href="https://arxiv.org/pdf/2103.03460">PDF</a>] [<a href="https://github.com/huitangtang/ViCatDA">Code</a>] [<a href="https://huitangtang.github.io/ViCatDA/">Page</a>]<br>
<div style="text-align: justify">
To promote categorical domain adaptation (CatDA), based on a joint category-domain classifier, 
we propose novel losses of adversarial training at both domain and category levels. 
Since the joint classifier can be regarded as a concatenation of individual task classifiers respectively for the two domains, 
our design principle is to enforce consistency of category predictions between the two task classifiers. 
Moreover, we propose a concept of vicinal domains whose instances are produced by a convex combination of pairs of instances respectively from the two domains. 
Intuitively, alignment of the possibly infinite number of vicinal domains enhances that of original domains.
</div>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/McDalNets.png"><img src='image/McDalNets.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>Unsupervised Multi-Class Domain Adaptation: Theory, Algorithms, and Practice</b><br>
<i>IEEE Transactions on Pattern Analysis and Machine Intelligence (TPAMI), 2022</i><br>
Yabin Zhang, Bin Deng, <b>Hui Tang</b>, Lei Zhang, and Kui Jia<br>
[<a href="https://arxiv.org/pdf/2002.08681">PDF</a>] [<a href="https://github.com/Gorilla-Lab-SCUT/MultiClassDA">Code</a>]<br>
<div style="text-align: justify">
Suggested by a new domain adaptation bound for unsupervised multi-class domain adaptation (multi-class UDA), 
we develop an algorithmic framework of Multi-class Domain-adversarial learning Networks (McDalNets), 
and its different instantiations via surrogate learning objectives either coincide with or resemble a few recently popular methods. 
Based on our identical theory for multi-class UDA, we also introduce a new algorithm of Domain-Symmetric Networks (SymmNets), 
which is featured by a novel adversarial strategy of domain confusion and discrimination.
</div>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/S2RDA.png"><img src='image/S2RDA.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>A New Benchmark: On the Utility of Synthetic Data with Blender for Bare Supervised Learning and Downstream Domain Adaptation</b><br>
<i>IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2023</i><br>
<b>Hui Tang</b> and Kui Jia<br>
[<a href="https://arxiv.org/pdf/2303.09165">PDF</a>] [<a href="https://github.com/huitangtang/On_the_Utility_of_Synthetic_Data">Code</a>] [<a href="https://huitangtang.github.io/On_the_Utility_of_Synthetic_Data/">Page</a>] [<a href="https://pan.baidu.com/s/1fHHaqrEHbUZLXEg9XKpgSg?pwd=w9wa">Dataset</a>]<br>
<div style="text-align: justify">
To solve the basic and important problems in the context of image classification, such as the lack of comprehensive synthetic data research and the insufficient exploration of synthetic-to-real transfer, we propose to exploit synthetic datasets to explore questions on model generalization, benchmark pre-training strategies for domain adaptation (DA), and <i>build a large-scale benchmark dataset S2RDA for synthetic-to-real transfer</i>, which can push forward future DA research.
</div>

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/STOCO.png"><img src='image/STOCO.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>Stochastic Consensus: Enhancing Semi-Supervised Learning with Consistency of Stochastic Classifiers</b><br>
<i>European Conference on Computer Vision (ECCV), 2022</i><br>
<b>Hui Tang</b>, Lin Sun, and Kui Jia<br>
[<a href="https://www.ecva.net/papers/eccv_2022/papers_ECCV/papers/136910319.pdf">PDF</a>] [<a href="https://github.com/huitangtang/STOCO">Code</a>] [<a href="https://huitangtang.github.io/STOCO/">Page</a>]<br>
<div style="text-align: justify">
We propose a new criterion based on consistency among multiple, stochastic classifiers, termed Stochastic Consensus (STOCO). 
Specifically, we model parameters of the classifiers as a Gaussian distribution whose mean and standard deviation are jointly optimized during training. 
We technically generate pseudo labels using a simple but flexible framework of deep discriminative clustering.
</div>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/GSF&PPF.png"><img src='image/GSF&PPF.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>Towards Discovering the Effectiveness of Moderately Confident Samples for Semi-Supervised Learning</b><br>
<i>IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR), 2022</i><br>
<b>Hui Tang</b> and Kui Jia<br>
[<a href="https://openaccess.thecvf.com/content/CVPR2022/papers/Tang_Towards_Discovering_the_Effectiveness_of_Moderately_Confident_Samples_for_Semi-Supervised_CVPR_2022_paper.pdf">PDF</a>] [<a href="https://github.com/huitangtang/GSF-PPF">Code</a>] [<a href="https://huitangtang.github.io/GSF-PPF/">Page</a>]<br>
<div style="text-align: justify">
We propose to utilize moderately confident samples. 
Based on the principle of local optimization landscape consistency, we propose Taylor expansion inspired filtration framework, 
relying on the Taylor expansion of the loss function to inspire the key measurement index of sample filtration, i.e., gradient and feature of finite orders. 
We derive two novel filters from this framework: gradient synchronization filter selecting samples with similar optimization dynamics to the most reliable one, 
and prototype proximity filter selecting samples near semantic prototypes.
</div>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/GSF&PPF.png"><img src='image/GSF&PPF.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>Towards Discovering the Effectiveness of Moderately Confident Samples for Semi-Supervised Learning</b><br>
<i>IEEE Transactions on Geoscience and Remote Sensing (TGRS), 2021</i><br>
Wenyuan Li, <b>Keyan Chen</b>, Hao Chen and Zhenwei Shi<br>
[<a href="http://levir.buaa.edu.cn/publications/Geographical_Knowledge-Driven.pdf">PDF</a>] [<a href="https://github.com/flyakon/Geographical-Knowledge-driven-Representaion-Learning">Code</a>]<br>
<div style="text-align: justify">
 We propose a Geographical Knowledge-driven Representation learning method for remote sensing images (GeoKR), improving network performance and reduce the demand for annotated data. The global land cover products and geographical location associated with each remote sensing image are regarded as geographical knowledge to provide supervision for representation learning and network pre-training.
</div>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/GAST.png"><img src='image/GAST.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>Geometry-Aware Self-Training for Unsupervised Domain Adaptation on Object Point Clouds</b><br>
<i>IEEE/CVF International Conference on Computer Vision (ICCV), 2021</i><br>
Longkun Zou, <b>Hui Tang</b>, Ke Chen, and Kui Jia<br>
[<a href="https://openaccess.thecvf.com/content/ICCV2021/papers/Zou_Geometry-Aware_Self-Training_for_Unsupervised_Domain_Adaptation_on_Object_Point_Clouds_ICCV_2021_paper.pdf">PDF</a>] [<a href="https://github.com/zou-longkun/GAST">Code</a>]<br>
<div style="text-align: justify">
We propose a novel Geometry-Aware Self-Training (GAST) method for unsupervised domain adaptation on object point sets, 
which encodes domain-invariant geometrics to semantic representation to mitigate domain discrepancy of point-based representations. 
Technically, based on self-paced self-training on unlabeled target data, our GAST integrates the self-supervised tasks of predicting rotation class and distortion location into representation learning, such that the domain-shared feature space can be constructed.
</div>

</div>
</div>
