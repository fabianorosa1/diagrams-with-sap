# diagram.py
from diagrams import Cluster, Diagram, Edge
from diagrams.aws.storage import S3
from diagrams.sap.other import PlaceholderServiceName
from diagrams.sap.integration import IntegrationSuite
from diagrams.sap.database_datamanagement import SAPHANACloud
from diagrams.sap.database_datamanagement import ObjectStore
from diagrams.sap.security import IdentityProvisioning
from diagrams.sap.analytics import SAPAnalyticsCloud
from diagrams.sap.runtimes import CloudFoundryRuntime
from diagrams.sap.database_datamanagement import SAPHANACloud

# SAP BTP Solution Diagrams and Icons guidelines colours
L0_BLUE_COLOUR = "#0070F2"
L0_FILLED_COLOUR = "#EBF8FF"
L1_BLUE_COLOUR = "#0040B0"
L1_FILLED_COLOUR = "#EBF8FF"
L1_BLUE_COLOUR = "#002A86"
SUCCESS_GREEN_COLOUR = "#188918"
SUCCESS_FILLED_COLOUR = "#F5FAE5"

FIX_GREY_COLOUR = "#7F7F7F"
NON_SAP_AREA_COLOUR = "#595959"

with Diagram("CIS Landscape", show=False, outformat="jpg", filename="my_diagram"):
    with Cluster("SAP Cloud Identity Services (CIS)", graph_attr= {"bgcolor": L0_FILLED_COLOUR, "pencolor": L0_BLUE_COLOUR, "fontname": "Verdana", "fontsize": "16"}):
        with Cluster("SAP Cloud Identity Services - Identity Authentication (IAS)", graph_attr= {"bgcolor": "white", "pencolor": L1_BLUE_COLOUR, "fontname": "Verdana", "fontsize": "16"}):
            sap_ias_ino = IdentityProvisioning("CIS_INO")

    with Cluster("Applications registered in CIS IAS"): 
        [SAPAnalyticsCloud("CISA_SAC") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_Y") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_X") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_A") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),

        CloudFoundryRuntime("CISA_BTPCF_B") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_C") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_D") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_E") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_F") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_G") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_H") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_I") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_J") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_L") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        CloudFoundryRuntime("CISA_BTPCF_M") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted"),
        SAPHANACloud("CISA_HANADB") >> Edge(label="use", color=FIX_GREY_COLOUR, style="dotted")] >> sap_ias_ino
    
    # with Cluster("SAP Business Technology Platform", graph_attr= {"bgcolor": L0_FILLED_COLOUR, "pencolor": L0_BLUE_COLOUR}):
    #     with Cluster("Subaccount", graph_attr= {"bgcolor": "white", "pencolor": L1_BLUE_COLOUR}):
    #         cloud_integration = IntegrationSuite("Cloud Integration")
    #        object_store = ObjectStore("Object Store")

    #         PlaceholderServiceName("Audit Log service") << Edge(label="Retrieves entries", color=FIX_GREY_COLOUR) << \
    #         cloud_integration >> Edge(color=FIX_GREY_COLOUR) >> SAPHANACloud("HANA Cloud")
    #         cloud_integration >> Edge(color=FIX_GREY_COLOUR) >> object_store
        
    # with Cluster("AWS", graph_attr= {"bgcolor": "white", "pencolor": NON_SAP_AREA_COLOUR}):
    #     object_store >> Edge(label="uses", color=FIX_GREY_COLOUR, style="dotted") >> S3("S3 Bucket")
