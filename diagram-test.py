from diagrams import Cluster, Diagram
from diagrams.onprem.vcs import Github
from diagrams.onprem.ci import Jenkins
from diagrams.aws.compute import Lambda

with Diagram("CXOne WFO Auto-Report", show=True, direction="LR"):

    with Cluster("Deployment"):
        deploy = [Github("github") >> Jenkins("jenkins") >> Lambda("lambda")]

    deploy
