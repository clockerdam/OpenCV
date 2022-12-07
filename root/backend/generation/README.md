# Resume-Builder

## Description
This project is a resume builder I developed for building a beautiful LaTeX typset resume from jsonresume conforming yaml data.  This allows for easy iteration and tracking of changes via diffs.  It also allows for the data itself to be used in any context where jsonresume is supported.

## Usage
* Ensure you have docker installed and running.
* Install builder requirements: `pip3 install builder/requirements.txt`
* Ensure you have jsonresume conforming yaml data in `data/`, to use mine clone the repo with: `git clone --recursive`.
* Build your pdf: `inv render --data={name-of-file}`.  *Do not include data/ path or .yaml suffix*

## Results
Here are some example's of the results, exported using `pdftoppm`.

![preview-page-1](preview-1.png)
![preview-page-2](preview-2.png)

## Showing off
And just because I'm a total nerd, here is an example of the text extracted from the pdf when running `pdftotext -layout {pdf_file}`.  This is great for ATS!

```
Joe Black
Experienced backend software engineer & python enthusiast
New York, NY       (646) 924-7718           me@joeblack.nyc            https://joeblack.nyc          joeblack949       joeblackwaslike


Summary
 Passionate engineer and linux expert with 7 years of experience seeking a backend engineering role where my expertise in
 python will help drive the success of a team and product that I genuinely believe in. I’m energetic, self-managed, determined,
 embody the principles of grit, and thrive in a fast-paced environment.

Awards
  Winner             Stanford Datajam, a hackathon sponsored by the US Department of Education. (2014)                    Palo Alto, CA

Skills
  Languages          Python 2 & 3, Bash, Javascript, GraphQL, Solidity, Golang, Ruby/Rails, Django, Flask, Starlette
  Technologies       SQL, NoSQL, Neo4j/Cypher, Redis, Airflow, ElasticSearch, Microservices, RESTful APIs, CI/CD, Git/Github, LATEX
  DevOps             Linux, Unix, Docker, Kubernetes, AWS, GCP, Ansible, Nginx


Work Experience
  Senior Python Engineer                                                                                             08/2019 – 03/2020
  Code & Theory                                                                                                           New York, NY
  • Brought in to work on the CNN Datacloud powering John King’s magic wall and the CNN election center.
  • Brought the Datacloud from POC to a production ready release which included the development of new ETL
    pipelines in Airflow and Neo4j, and a custom ORM-like OGM framework based on Neomodel capable of auto-
    generating it’s own detailed documentation.
  • Architected and developed an ASGI geospatial-temporal data microservice with interactive documentation and
    playground using python, postGIS, GeoAlchemy, Starlette, Fast-API, and swagger.
  • Spearheaded an internal tech-leadership project that taught and mentored python engineers of all experience
    levels across multiple continents.
  • Architected and developed a new declarative automation-testing framework in pytest and selenium that dynam-
    ically detects a page’s components and builds all test cases dynamically.

  Senior Software Engineer                                                                                           04/2019 – 08/2019
  See-Thru Healthcare                                                                                                     Brooklyn, NY
  • Lead the architecture and development efforts for a new group tele-therapy platform.
  • Drove key architectural decisions regarding data modeling and API design, technologies leveraged, and third-
    party integrations to maximize the effeciency of a small development team.
  • Architected and implemented a unified identity provider using AWS Cognito, enabling a seamless user registra-
    tion and login experience across products while directing growth to the core product.
  • Designed and implemented a GraphQL & Relay API using python and graphene that drove the development of
    more modular, declarative, and reusable componentry in the front-end react application.

  Co-founder & Senior Software Engineer                                                                              06/2017 – 12/2018
  Telephone                                                                                                               New York, NY
  • Co-founded a start-up to fund and develop a privacy-focused decentralized communications app.
  • Collaboratively architected a decentralized protocol and app using ethereum, solidity, python, and javascript.
  • Educated and advised co-founders on the constraints posed by decentralized architecture and the ICO funding
    process to better align the vision of the company and viability of the product.
  • Designed a decentralized services marketplace to incentivize the development of new features, build community,
    and support the underlying token economy.

 Contract Software Engineer                                                                                               04/2014 – 04/2019
 Black Limited                                                                                                                  New York, NY
  • Founded a development and consulting company which I use for short-term contract work referred to me.
  • Developed and deployed a privacy-focused crypto-commerce platform using python, flask, and bitcoin.
  • Developed tools in python used by the Security Scorecard platform for IP attribution of vendors.
  • Leveraged NTLK to identify inconsistencies across legal contracts for a law firm specializing in foreclosures.
  • Developed open-source python projects such as the official BTCPay python client, GPGKeyring, and Pricing.

 Senior Software Engineer & DevOps                                                                                        08/2015 – 06/2017
 Call for America, LLC                                                                                                          New York, NY
  • Built and maintained a bare-metal kubernetes-based infrastructure to scale the Kazoo cloud PBX platform.
  • Slashed maintenance costs over 50% by automating the deployment and maintenance of critical infrastructure
    using docker, kubernetes, python, and bash.
  • Developed and implemented custom tools for containerizing self-configuring microservices using python, bash,
    C, and golang.
  • Increased platform stability over 30% by spearheading the development of tooling for spec-testing containers
    using bash and goss.

 Co-founder & Software Engineer                                                                                           06/2013 – 08/2015
 Unorthodox, LLC                                                                                                           San Francisco, CA
  • Co-founded and developed a small data-driven email-marketing platform with real-time analytics in python.
  • Improved delivery over 50% using MTA throttling based on provider history, IP reputation, and SMTP reject codes.
  • Implemented real-time analytics to improve campaign insights using python, AWS, URL redirection, and kibana.
  • Increased targeting relevancy over 100% by enriching existing demographic data using third-party data append
    APIs such as TowerData and FullContact.


Extracurricular Activities
 Mentor                                                                                                                          2013 – 2015
 Noisebridge Hackerspace                                                                                                   San Francisco, CA
  • Mentored hackers and students from local universities and code bootcamps with various engineering related
    projects and tasks.

 Speaker                                                                                                                                 2014
 HackMiami Conference                                                                                                              Miami, FL
  • Delivered a bio-hacking talk discussing the usage of various technologies, proteins, and growth factors for cog-
    nitive enhancement with the co-founder of Hack Miami.


Education
 Computer Science                                                                                                           Indianapolis, IN
 Ivy Tech College


Open Source Projects
 BTCPay-python                                                                                  https://github.com/btcpayserver/btcpay-python
 The official python client for the BTCPay Server API, an open-source payment processor for bitcoin and litecoin.
 python, cryptocurrency, bitcoin, RESTful APIs, BTCPay

 TmplD                                                                                                https://github.com/joeblackwaslike/tmpld
 Advanced configuration templating in jinja2 using cluster state for self-configuring, containerized, microservice architectures.
 python, containers, docker, kubernetes, jinja2, configuration, microservices
```



