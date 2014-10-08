IDCOAS
======

Infectious Disease Correlation and Outbreak Alerting System

Project goals:
+ Consume sample data into OSSIM (create custom plugin)... DONE
+ Create correlation rules to alert based on frequency of certain types of pathogens ...DONE
+ Split logs off to ElasticSearch instance for more dashboards, trends
+ Use OpenGraphiti to visualize information (will require special export script to feed into OpenGraphiti's format) … Not done :-(
+ Create heat maps for outbreaks over time ...DONE
+ Create an outbreak simulator to generate detection events for feeding into OSSIM and OpenGraphiti ...DONE

NOTE: This is all sample data, not harvested from any sort of real occurrence or disease outbreak.

![Project Drawing](https://raw.github.com/ashmastaflash/IDCOAS/master/ProjectDrawing.jpg)
![Initial Outbreak](https://raw.github.com/ashmastaflash/IDCOAS/master/prettystuff/Screenshots/InitialOutbreak.png)
![Trend Graph](https://raw.github.com/ashmastaflash/IDCOAS/master/prettystuff/Screenshots/StackTrend.png)
![Line Graph](https://raw.github.com/ashmastaflash/IDCOAS/master/prettystuff/Screenshots/LineTrend.png)
![Alarms](https://raw.github.com/ashmastaflash/IDCOAS/master/prettystuff/Screenshots/Alarms.png)
![Correlated Events](https://raw.github.com/ashmastaflash/IDCOAS/master/prettystuff/Screenshots/CorrelatedEvents.png)

Participants:
+ @FraleyLab
+ @ashmastaflash
  
  
