# Bayesian-Spam-Filter
a Content Based Filtering Technique this approach creates automatic filtering rules and classifies emails using machine learning approaches here we will be using the Naïve Bayesian classification which has been adopted to detect and control spam.
Abstract:
Nowadays Email communications is an essential service and has been greatly abused by spammers to spread malicious content, the most popular types of blatantly criminal spam are Nigerian letters and phishing that some users may fall prey to while causing others irritation and wasting their time. The distribution of spam has been improved in the past few years due to the improvement in internet technology. To counter the ever-growing issue of spam effective countermeasures need to be taken. Machine learning methods of recent are being used to successfully detect and filter spam emails. 
In this project we will using a Content Based Filtering Technique this approach creates automatic filtering rules and classifies emails using machine learning approaches here we will be using the Naïve Bayesian classification which has been adopted to detect and control spam.
We were successful in our attempt at implementing and training a model which had a detection rate of 92.3%, a false positive rate of 0.7% and an overall accuracy of 95.7%.

Introduction:
Spam is usually said to be unsolicited usually commercial messages (such as emails, text messages, or Internet postings) sent to many recipients or posted in a large number of places. In simple words it can be termed as unwanted e-mail. Statistics show that nearly 85% of all emails are spam. Apart from wasting time, spam costs money to users with dial-up connections, wastes bandwidth, and may expose under-aged recipients to unsuitable content.
Anti-spam is software that aims to detect and block potentially dangerous email from user inboxes. It helps protect the confidentiality, integrity and availability of an individual user or an organization.
Anti-spam filters are one such way to implement anti-spamming they vary in functionality from Challenge/response Systems to content-based filters. The latter are generally more powerful, as spammers often spoof their IP’s and are coming up with various ways to circumvent pre-existing measures that have been in place for a long time. Content-based filters search for keyword patterns in the messages. These patterns need to be crafted by hand, and to achieve better results they need to be tuned to each user and to be constantly maintained which is a tedious tome consuming task, requiring expertise that an average user may not possess. Statistical, or Bayesian, filtering once set up requires no administrative maintenance. Instead, users mark messages as spam or non-spam and the filtering software learns from these judgements. Thus, it is matched to the end user's needs, and if users consistently mark/tag the emails, can respond quickly to changes in spam content.
Some Relevant Spam Statistics
In the following subsections, we will highlight some worldwide statistical observations. Besides, some country specific metrics will also be discussed.
•	As of 2018 approximately 236 billion emails are exchanged daily
•	2018 saw an average of 14.5 billion spam emails daily
•	Email spam costs businesses $20.5 billion every year.
•	Scams and fraud comprise only 2.5% of all spam email however, phishing statistics indicate that identity theft makes up 73% of this figure.
•	As many as 85% of all organizations have been targeted by phishing scams in 2021.
•	Microsoft accounts are the most popular targets of phishing emails, accounting for 43% of all phishing attempts.
•	United States has traditionally been the largest source of spam, however, in recent times it is not the case anymore. Though there were legislations such as CAN-SPAM (Controlling the Assault of Non-Solicited Pornography and Marketing Act) to protect the users, it did not have the expected deterrent effect on the spammers. USA houses world’s top 70% spam gangs, responsible for coordinated worldwide spamming.
•	As of April 2019, Brazil and Russia have conveniently overtaken USA and China (another substantial spam originating country), to produce approximately 16% and 14% of total volume of worldwide spam.

Motivation to explore the area 
The field of anti-spamming is a fight between spammers trying to come up with new ways to circumvent current solutions and security specialists trying to thwart them at every step as the current anti-spam measures are mostly lagging behind the innovativeness of spammers. 
Motivation behind this project was to analyze initiative is to address a gap that has risen over time in the field of spam email detection. We have discussed several existing approaches for anti-spamming techniques and highlighted the loopholes and the current situation. we have implemented a machine-learning based approach to anti-spamming as the current anti-spam measures have not been successful in their attempts to stop spam, we believe this justifies a shift towards machine learning based anti-spam approaches to be more widely in use as they can be tailored to specifically protect against spam emails and ha.
Significant use cases
•	On the level of an Individual user:
o	Anti-spam software also helps prevent malicious emails that trick users to divulge personal and confidential information. 
o	It is one of the best ways to avoid malware and viruses, as there’s no opportunity to click on the harmful links included in some spam mail.
o	Anti-spam software “declutters” email inboxes, reducing emails that are distracting and time-wasting.
o	It blocks potential threats so that the end user doesn’t have to deal with them and come to a decision.
o	it’s essential for users who may not be very knowledgeable about IT or cybersecurity hazards

•	Importance of Anti-spamming for a Business/Organization
o	Provides an additional layer of protection 
	Will help prevent different types of attacks and threats, such as spam, phishing, and malware, including ransomware, virus, and trojan.
o	Many businesses are subject to strict privacy and data storage regulations
	Is true especially if they deal with sensitive or confidential information. 
	To continue operations, they may have to meet certain conditions including always using spam filtering to reduce the risk of data breaches.
o	Protect your business’s reputation 
o	A security breach can be extremely damaging for a business’s reputation, especially if client data is compromised. 
o	Anti-spam software helps ensure this doesn’t occur, by increasing security and filtering out potentially harmful emails.

Background/related work:
Challenge/response systems
•	Originally designed in 1997 by Stan Weatherby
•	Called Email Verification
•	A challenge–response system is a type of spam filter that automatically sends a reply with a challenge to the sender of an incoming e-mail.
o	In this reply, the purported sender is asked to perform some action to assure delivery of the original message, which would otherwise not be delivered. 
o	The action to perform typically takes relatively little effort to do once, but great effort to perform in large numbers.
•	Senders that have previously performed the challenging action, or who have previously been sent e-mail(s) to, would be automatically whitelisted.
•	Various Challenges used in challenge response system
o	Simply sending an (unmodified) reply to the challenging message. 
o	A challenge that includes a web URL
	which can be loaded in an appropriate web browsing tool to respond to the challenge, so simply clicking on the link is sufficient to respond to the challenge.
o	A challenge requiring reading natural language instructions on how to reply, with a special string or passcode in the reply. 
o	For example, converting a date string (such as 'Thu Jan 12 08:45:44 2012') into its corresponding timestamp (1326379544). 
o	Systems can attempt to produce challenges for which auto response is very difficult, or even an unsolved Artificial Intelligence problem.
o	example is a "CAPTCHA" test in which the sender is required to view an image containing a word or phrase and respond with that word or phrase in text.
•	Drawbacks
o	Many senders will find the additional burden annoying.
o	The requirements of the challenge may also be too confusing or simply go unread, causing messages to be delayed or go completely unconfirmed. 
o	They don’t reject unsolicited bulk email at the SMTP layer.
o	Although C/R systems are simple to implement and don't require any software updates, they have numerous weaknesses when applied as anti-spam systems:
	Misplaced Burden
•	Burden of anti-spam system placed on senders
•	One should not place the burden of an anti-spam system on the sender. 
•	Any legitimate e-mail, where the C/R system mistakenly places the burden on an innocent sender to confirm incoming e-mail so that the recipient doesn't have to review any unconfirmed e-mail messages.
•	The recipient is receiving a benefit, which the sender is paying for
	Automated Messages are hard to confirm
•	many automated systems don't offer enough information to discern what e-mail address the automated e-mail messages will come from.
	System Stalemates
•	If the sender and recipient both use challenge/response systems, the two entities may never be able to communicate.
	Confirmations Are Easily Defeated
	Challenges Cause Abuse
•	A spammer could easily use the challenge/response system to bombard a victim with challenges by sending a large amount of e-mail messages to the C/R system that appear to be from the victim's e-mail address
	Spam Is Still Accepted
•	Even though spam may not show up at the challenge/response system's inbox, the e-mail is accepted from the spammer for delivery.
•	E-mail from spammers should be rejected at the SMTP layer
Checksum based filtering
•	Checksum-based filter exploits the fact that the emails are sent in bulk, that is that they will be identical with small variations. 
•	Checksum-based filters strip out everything that might vary between emails, reduce what remains to a checksum (checksum is calculated using a hash function), and look that checksum up in a database.
•	such as the Distributed Checksum Clearinghouse which collects the checksums of emails that email recipients consider to be spam (some people have a button on their email client which they can click to nominate a message as being spam)
•	If the checksum is in the database, the message is likely to be spam. 
•	Advantages
o	It lets ordinary users help identify spam, and not just administrators, thus vastly increasing the pool of spam fighters.
•	Drawbacks
o	To avoid being detected in this way, spammers will sometimes insert unique invisible gibberish known as hashbusters into the middle of each of their emails.
o	This makes each message have a unique checksum.
DNS-based blacklists
•	A Domain Name System blocklist is a service for operation of mail servers to perform a check via a Domain Name System (DNS) query 
•	whether the sending host's IP address is blacklisted for email spam.
•	Most mail server software can be configured to check such lists, typically rejecting or flagging emails from such sites.
•	Working
o	When a mail server receives a connection from a client, and wishes to check that client against a DNSBL it does the following: 
	Take the client's IP address and reverse the order of octets
	Append the DNSBL's domain name
	Look up this name in the DNS as a domain name 
	This will return either an address, indicating that the client is listed; or an "NXDOMAIN" ("No such domain") code, indicating that the client is not. 
•	Drawbacks
o	Legitimate emails blocked along with spam from shared mail servers
o	Lists of dynamic IP addresses
o	Lists that include "spam-support operations “
o	Some lists have unclear listing criteria and delisting may not happen automatically nor quickly.
o	Because lists have varying methods for adding IP addresses and/or URIs, it can be difficult for senders to configure their systems appropriately to avoid becoming listed on a DNSBL.
Statistical content filtering
•	These systems primarily rely on the examination of the body or content of the email
•	A common class of spam detectors for quite some time now has been the ‘Content based Filtering’ method and several of its variations. 
•	In these systems, a thorough analysis is done on the host message to find out patterns in message texts, these are then matched with predefined and confirmed spam patterns and a score is recorded. 
•	A decision of spam or ham is taken after comparing the cumulative score against a threshold value.
•	One such method is Bayesian filtering is one of the most effective and intelligent solutions to filter spam emails nowadays. Bayesian filters must be “trained to work effectively”. After training, to classify an email message as spam, one can check if it exceeds a specific threshold
•	Advantages:
o	Statistical, or Bayesian, filtering once set up requires no administrative maintenance
o	Instead, users mark messages as spam or non-spam and the filtering software learns from these judgements. 
o	It is matched to the end user's needs, and if users consistently mark/tag the emails, can respond quickly to changes in spam content.
o	Can be trained on a per-user basis.
o	Has low rate of false positives (where legitimate email is incorrectly classified as spam).
o	The word probabilities are unique to each user 
	Therefore, it can evolve over time with corrective training whenever the filter incorrectly classifies an email. 
	As a result, Bayesian spam filtering accuracy after training is often superior to pre-defined rules.
•	Disadvantages
o	May be susceptible to Bayesian poisoning.
	A spammer practicing Bayesian poisoning will send out emails with large amounts of legitimate text
	Spammer tactics include insertion of random innocuous words that are not normally associated with spam.
	Thereby decreasing the email's spam score, making it more likely to slip past a Bayesian spam filter.
o	Technique used to try to defeat Bayesian spam filters is to replace text with pictures. 
	The whole text of the message, or some part of it, is replaced with a picture where the same text is "drawn". 
	The spam filter is usually unable to analyze this picture.
URL filtering
•	Most spam/phishing messages contain an URL that they entice victims into clicking on. Thus, a popular technique since the early 2000s consists of extracting URLs from messages and looking them up in databases such as Spamhaus' Domain Block List (DBL), SURBL, and URIBL
Country-based filtering
•	Some email servers expect to never communicate with particular countries from which they receive a great deal of spam. Therefore, they use country-based filtering – a technique that blocks email from certain countries. This technique is based on country of origin determined by the sender's IP address rather than any trait of the sender.
Honeypots
•	Another approach is simply creating an imitation MTA that gives the appearance of being an open mail relay, or an imitation TCP/IP proxy server that gives the appearance of being an open proxy. Spammers who probe systems for open relays and proxies will find such a host and attempt to send mail through it, wasting their time and resources, and potentially, revealing information about themselves and the origin of the spam they are sending to the entity that operates the honeypot. Such a system may simply discard the spam attempts, submit them to DNSBLs, or store them for analysis by the entity operating the honeypot that may enable identification of the spammer for blocking.
Hybrid filtering
•	SpamAssassin, Policyd-weight and others use some or all of the various tests for spam and assign a numerical score to each test. Each message is scanned for these patterns, and the applicable scores tallied up. If the total is above a fixed value, the message is rejected or flagged as spam. By ensuring that no single spam test by itself can flag a message as spam, the false positive rate can be greatly reduced.
Outbound spam protection
•	Outbound spam protection involves scanning email traffic as it exits a network, identifying spam messages and then taking an action such as blocking the message or shutting off the source of the traffic. While the primary impact of spam is on spam recipients, sending networks also experience financial costs, such as wasted bandwidth, and the risk of having their IP addresses blocked by receiving networks.
Outbound spam protection not only stops spam, but also lets system administrators track down spam sources on their network and remediate them – for example, clearing malware from machines which have become infected with a virus or are participating in a botnet.

After researching on the topic, we decided to implement Content filtering using a Naive Bayesian approach
Technical details of the project:
How the naive Bayes classifier is used to filter spam
•	The Naïve Bayes theorem is used twice:
o	The First time is to compute the “Spamicity” of a word
o	The Second time to consider the “Spamicity” of several words and combine their “Spamicity” to determine a message's overall probability of being spam.
o	Sometimes Used to deal with rare word (but we will not be using this here)

Computing the probability that a message containing a given word is spam
•	Let's suppose the suspected message contains the word "geass".
•	the probability that a message containing a given word is spam is given by:
 
•	Where:
o	P(S|W) is the probability that a message is a spam, knowing that the word "geass" is in it
o	Pr(S) the overall probability that any given message is spam
o	Pr(W|S) is the probability that the word "geass" appears in spam emails
o	Pr(H) is the overall probability that any given message is not spam
o	Pr(W|H) is the probability that the word "geass" appears in ham emails.
•	Statistics show that the current probability of any message being spam is 80%, at the very least
 
•	Most Bayesian spam detection software assumes that there is no a priori
o	That is reason for any incoming message to be spam rather than ham, and considers both cases to have equal probabilities of 50%
 
o	Filters using the above Hypothesis are known as “not biased”
•	This Simplifies the previous formula to:
 
•	Functionally equivalent to asking, "what percentage of occurrences of the word "geass" appear in spam emails
•	This quantity is called "spamicity" of the word "geass"
•	The number Pr(W|S) used in this formula is approximated to the frequency of emails containing "geass" in the emails identified as spam during the learning phase. 
•	Similarly, Pr(W|H) is approximated to the frequency of emails containing "geass" in the emails identified as ham during the learning phase. 
•	For these approximations to make sense, the set of emails needs to be big and representative enough. 
•	It is also advisable that the data set of emails conforms to the 50% hypothesis about repartition between spam and ham.
o	This means that the number of spam and ham emails in the data set need to be equal in order to line up with the “nonbiased” hypothesis we have taken.
o	Our training set consists of a total of 702 mails
	With 260 mails divided equally between spam and ham
Combining individual probabilities
•	Determining whether a message is spam or ham based only on the presence of the word "geass" is inherently prone to error.
•	Thus, we consider several words and combine their spamicity to determine a message's overall probability of being spam.
 
•	Where:
o	p is the probability that the suspect email is spam
o	p1 is the probability p(W1|S) that the first word (for example "geass") appears, given that the email is spam
o	p2 is the probability p(W2|S) that the second word (for example “gate") appears, given that the email is spam
o	This occurs for n such words.
•	Spam filtering software based on this formula is sometimes referred to as a naive Bayes classifier, as "naive" refers to the strong independence assumptions between the features
 
Email Spam Filtering Technique Implementation
•	Pre-processing
•	Building word dictionary
•	Feature Extraction
•	Training and testing Classifier

 
Pre-processing Stage
•	Pre-processing of the Ling-spam corpus dataset:
•	Each file has a subject and a body we extracted the body from the txt file and performed the following on it:
o	Lemmatization
	The process of grouping together the different inflected forms of a word so they can be analyzed as a single item 
	Each word is run through the code which returns then stores the word in its common base form
o	Removal of stop words non-words and special characters
	A set called “stop_words” which contained English stop words was used. 
	The contents of the original file where then erased and then words which were not present in “stop_words” and non-words where not rewritten into the txt file after lemmatization
 
Building word dictionary
•	A word dictionary basically contains all the words used in the data set provided to it and contains the frequency of each word across the entire data set.
•	We have chosen to exclude all words with length less than 3 and have taken 3000 of the most common words to make the word dictionary.
•	Sample Output with 30 of the most common words from our word dictionary after performing word dictionary building on 702 preprocessed emails
 
Feature Extraction
•	Feature extraction refers to the process of transforming raw data into numerical features that can be processed while preserving the information in the original data set. It yields better results than applying machine learning directly to the raw data.
•	Feature Extraction aims to reduce the number of features in a dataset by creating new features from the existing ones (and then discarding the original features).
•	These new reduced set of features should then be able to summarize most of the information contained in the original set of features. In this way, a summarized version of the original features can be created from a combination of the original set.
•	Once the word dictionary is complete, we can extract an n-dimensional word count vector (the specific feature extracted in this project) for each email in the training set. The frequency of n words in the training file is represented by each word count vector.
•	Most of the values tend to be zero in the frequency list.
•	EXAMPLE: -
o	Suppose we have x words in our dictionary. Each word count vector contains the frequency of x dictionary words in the training file. 
•	A matrix is created in which each unique word is represented by a column of the matrix, and each text sample from the document is a row in the matrix. The value of each cell is nothing but the count of the word in that text sample.
•	Let us consider a few sample texts from a document
•	document = [ “One Student helps Two Students”, “Two Students help Four Students”, “Each Student helps many other Students at College.”]
	at	each	four	student	students	college	help	helps	many	one	Other	two
Document 1	0	0	0	1	1	0	0	1	0	0	0	1
Document 2	0	0	1	0	2	0	1	0	0	0	0	1
Document 3	1	1	0	1	1	1	0	1	1	0	1	0

•	All of the data above would be put in the form of a nested array with each separate array within the larger array representing the features of a particular document.
•	The words are not kept as strings when the feature extraction procedure is completed. Rather, they are assigned a certain index value. The number of occurrences of the jth word in the dictionary in the ith file will be the value at index 'ij.' In this scenario, index 0 would be assigned to 'at,' index 1 to 'each,' index 2 to 'four,' and so on.
Training and testing Classifier
•	The training and testing of the classifier was done on 260 emails out of which 130 are ham and 130 were spam emails.
•	The classifier Identified 1 HAM email as SPAM and 10 SPAM emails as HAM the rest of the identification was correct.
Experimental Results:
 
Observations:
•	True Positives (TP): The number of spam emails classified as spam.
•	 TP = 120 
•	True Negatives (TN): The number of ham emails classified as ham.
•	TN = 129
•	False Positives (FP): The number of ham falsely classified as spam.
•	FP = 1 
•	False Negatives (FN): The number of spam falsely classified as ham.
•	FN = 10
•	Detection Rate (DR): TP / (TP + FN).
•	DR = 0.923
•	False positive Rate (FPR): FP/ (TN + FP).
•	FPR = 0.007
•	Overall Accuracy (OA): (TP + TN) / (TP + FP + FN +TN).
•	OA= 0.957
