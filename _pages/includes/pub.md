
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
[<a href="https://arxiv.org/pdf/2303.09165">PDF</a>] [<a href="https://github.com/huitangtang/On_the_Utility_of_Synthetic_Data">Code</a>] [<a href="https://huitangtang.github.io/On_the_Utility_of_Synthetic_Data/">Page</a>]<br>
<div style="text-align: justify">
To solve the basic and important problems in the context of image classification, such as the lack of comprehensive synthetic data research and the insufficient exploration of synthetic-to-real transfer, we propose to exploit synthetic datasets to explore questions on model generalization, benchmark pre-training strategies for DA, and <i>build a large-scale benchmark dataset S2RDA for synthetic-to-real transfer</i>, which can push forward future domain adaptation research.
</div>

</div>
</div>



<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/DRENet.png"><img src='image/DRENet.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>A Degraded Reconstruction Enhancement-based Method for Tiny Ship Detection in Remote Sensing Images with A New Large-scale Dataset</b><br>
<i>IEEE Transactions on Geoscience and Remote Sensing (TGRS), 2022</i><br>
Jianqi Chen, <b>Keyan Chen</b>, Hao Chen, Zhengxia Zou and Zhenwei Shi<br>
[<a href="http://levir.buaa.edu.cn/publications/DRENet.pdf">PDF</a>] [<a href="https://github.com/WindVChen/DRENet">Code</a>] [<a href="https://github.com/windvchen/levir-ship">Dataset</a>]<br>
<div style="text-align: justify">
We propose a tiny ship detection method namely, Degraded Reconstruction Enhancement Network (DRENet), for medium-resolution remote sensing images, and introduce Levir-Ship, which contains 3876 GF-1/GF-6 multi-spectral images and over 3K tiny ship instances.
</div>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/P2Net.png"><img src='image/P2Net.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>Contrastive Learning for Fine-grained Ship Classification in Remote Sensing Images</b><br>
<i>IEEE Transactions on Geoscience and Remote Sensing (TGRS), 2022</i><br>
Jianqi Chen, <b>Keyan Chen</b>, Hao Chen, Wenyuan Li, Zhengxia Zou, and Zhenwei Shi<br>
[<a href="http://levir.buaa.edu.cn/publications/CLFSC.pdf">PDF</a>] [<a href="https://github.com/WindVChen/Push-and-Pull-Network">Code</a>]<br>
<div style="text-align: justify">
We propose an asynchronous contrastive learning-based method for effective fine-grained ship classification, which refers to as "Push-and-Pull Network (P2Net)", includes a "push-out stage" and a "pull-in stage", where the first stage forces all the instances to be de-correlated and then the second one groups them into each subclass.
</div>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/GeoKR.png"><img src='image/GeoKR.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>Geographical Knowledge-Driven Representation Learning for Remote Sensing Images</b><br>
<i>IEEE Transactions on Geoscience and Remote Sensing (TGRS), 2021</i><br>
Wenyuan Li, <b>Keyan Chen</b>, Hao Chen and Zhenwei Shi<br>
[<a href="http://levir.buaa.edu.cn/publications/Geographical_Knowledge-Driven.pdf">PDF</a>] [<a href="https://github.com/flyakon/Geographical-Knowledge-driven-Representaion-Learning">Code</a>]<br>
<div style="text-align: justify">
 We propose a Geographical Knowledge-driven Representation learning method for remote sensing images (GeoKR), improving network performance and reduce the demand for annotated data. The global land cover products and geographical location associated with each remote sensing image are regarded as geographical knowledge to provide supervision for representation learning and network pre-training.
</div>

</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge"></div><a href="image/STT.png"><img src='image/STT.png' alt="sym" width="100%"></a></div></div>
<div class='paper-box-text' markdown="1">

<b>Building Extraction from Remote Sensing Images with Sparse Token Transformers</b><br>
<i>Remote Sensing, 2021</i><br>
<b>Keyan Chen</b>, Zhengxia Zou and Zhenwei Shi<br>
[<a href="https://www.mdpi.com/2072-4292/13/21/4441">PDF</a>] [<a href="https://github.com/KyanChen/STT">Code</a>] [<a href="https://kyanchen.github.io/STT/">Page</a>] [<a href="https://huggingface.co/spaces/KyanChen/BuildingExtraction">Demo</a>]<br>
<div style="text-align: justify">
We propose STT to explore the potential of using transformers for efficient building extraction. STT conducts an efficient dual-pathway transformer that learns the global semantic information in both their spatial and channel dimensions and achieves state-of-the-art accuracy on two building extraction benchmarks.
</div>

</div>
</div>
