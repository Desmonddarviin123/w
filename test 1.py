Python 3.6.3 (v3.6.3:2c5fed8, Oct  3 2017, 17:26:49) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import bs4
>>> import requests
>>> res = requests.get('https://en.wikipedia.org/wiki/Machine_learning')
>>> type(res)
<class 'requests.models.Response'>
>>> soup = bs4.BeautifulSoup(res.text, 'lxml')
>>> type(soup)
<class 'bs4.BeautifulSoup'>
>>> soup.select('.mw-headline')
[<span class="mw-headline" id="Overview_of_Machine_Learning">Overview of Machine Learning</span>, <span class="mw-headline" id="Machine_learning_tasks">Machine learning tasks</span>, <span class="mw-headline" id="History_and_relationships_to_other_fields">History and relationships to other fields</span>, <span class="mw-headline" id="Relation_to_data_mining">Relation to data mining</span>, <span class="mw-headline" id="Relation_to_optimization">Relation to optimization</span>, <span class="mw-headline" id="Relation_to_statistics">Relation to statistics</span>, <span class="mw-headline" id="Theory"><span id="Generalization"></span> Theory</span>, <span class="mw-headline" id="Approaches">Approaches</span>, <span class="mw-headline" id="Types_of_learning_algorithms">Types of learning algorithms</span>, <span class="mw-headline" id="Supervised_and_semi-supervised_learning">Supervised and semi-supervised learning</span>, <span class="mw-headline" id="Unsupervised_learning">Unsupervised learning</span>, <span class="mw-headline" id="Reinforcement_learning">Reinforcement learning</span>, <span class="mw-headline" id="Processes_and_techniques">Processes and techniques</span>, <span class="mw-headline" id="Feature_learning">Feature learning</span>, <span class="mw-headline" id="Sparse_dictionary_learning">Sparse dictionary learning</span>, <span class="mw-headline" id="Anomaly_detection">Anomaly detection</span>, <span class="mw-headline" id="Decision_trees">Decision trees</span>, <span class="mw-headline" id="Association_rules">Association rules</span>, <span class="mw-headline" id="Models">Models</span>, <span class="mw-headline" id="Artificial_neural_networks">Artificial neural networks</span>, <span class="mw-headline" id="Support_vector_machines">Support vector machines</span>, <span class="mw-headline" id="Bayesian_networks">Bayesian networks</span>, <span class="mw-headline" id="Genetic_algorithms">Genetic algorithms</span>, <span class="mw-headline" id="Applications">Applications</span>, <span class="mw-headline" id="Limitations">Limitations</span>, <span class="mw-headline" id="Bias">Bias</span>, <span class="mw-headline" id="Model_assessments">Model assessments</span>, <span class="mw-headline" id="Ethics">Ethics</span>, <span class="mw-headline" id="Software">Software</span>, <span class="mw-headline" id="Free_and_open-source_software">Free and open-source software</span>, <span class="mw-headline" id="Proprietary_software_with_free_and_open-source_editions">Proprietary software with free and open-source editions</span>, <span class="mw-headline" id="Proprietary_software">Proprietary software</span>, <span class="mw-headline" id="Journals">Journals</span>, <span class="mw-headline" id="Conferences">Conferences</span>, <span class="mw-headline" id="See_also">See also</span>, <span class="mw-headline" id="References">References</span>, <span class="mw-headline" id="Further_reading">Further reading</span>, <span class="mw-headline" id="External_links">External links</span>]
>>> for i in soup.select('.mw-headline'):
	print (i.text)

	
Overview of Machine Learning
Machine learning tasks
History and relationships to other fields
Relation to data mining
Relation to optimization
Relation to statistics
 Theory
Approaches
Types of learning algorithms
Supervised and semi-supervised learning
Unsupervised learning
Reinforcement learning
Processes and techniques
Feature learning
Sparse dictionary learning
Anomaly detection
Decision trees
Association rules
Models
Artificial neural networks
Support vector machines
Bayesian networks
Genetic algorithms
Applications
Limitations
Bias
Model assessments
Ethics
Software
Free and open-source software
Proprietary software with free and open-source editions
Proprietary software
Journals
Conferences
See also
References
Further reading
External links

>>> 
