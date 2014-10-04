IDCOAS
======

Infectious Disease Correlation and Outbreak Alerting System

Project goals:
+ Consume sample data into OSSIM (create custom plugin)... DONE
+ Create correlation rules to alert based on frequency of certain types of pathogens ...DONE
+ Either use OTX threat map or create simple heatmap from information in OSSIM's DB
+ Split logs off to ElasticSearch instance for more dashboards and API to pull data to feed into OpenGraphiti
+ Use OpenGraphiti to visualize information (will require special export script to feed into OpenGraphiti's format)
+ Create an outbreak simulator to generate detection events for feding into OSSIM and OpenGraphiti ...DONE
  
  
