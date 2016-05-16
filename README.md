# xld-bulk-restarts-plugin

## Usage
After installation you will be able to right click on any Folder and execute this Control Task. It will find any Tomcat Server (tomcat.Server type) in the subdirectories under it and invoke the 'stop' on them. After all the stop jobs completed (or failed), it will execute the 'start' control tasks on them. 

### Example output

````
> Found Tomcat containers: [Infrastructure/folder/gdgf/host1/tc1 [tomcat.Server], Infrastructure/folder/host2/tc1 [tomcat.Server], Infrastructure/folder/gdgf/host1/tc2 [tomcat.Server], Infrastructure/folder/gdgf/host1/tc3 [tomcat.Server], Infrastructure/folder/host2/tc3 [tomcat.Server], Infrastructure/folder/host2/tc99 [tomcat.Server]]

> Executing Control task [stop] for Infrastructure/folder/gdgf/host1/tc1, task id f51eee3a-0422-4a07-9d0e-5ce60326c464

> Executing Control task [stop] for Infrastructure/folder/host2/tc1, task id 6a851133-2cb3-4cea-a5b8-5ac473582ac9

> Executing Control task [stop] for Infrastructure/folder/gdgf/host1/tc2, task id f7135d43-3eb4-40ac-bedb-7dab64525368

> Executing Control task [stop] for Infrastructure/folder/gdgf/host1/tc3, task id 3f204e07-1036-4cbb-8b58-b2ee96ce56a5

> Executing Control task [stop] for Infrastructure/folder/host2/tc3, task id 424d6a10-5304-4814-a697-67aa683158c9

> Executing Control task [stop] for Infrastructure/folder/host2/tc99, task id cebad781-fde6-4cbb-b9fd-a03ad1c4e402

> Waiting for task f51eee3a-0422-4a07-9d0e-5ce60326c464 to finish

> Executing Control task [start] for Infrastructure/folder/gdgf/host1/tc1, task id d407f392-5a40-45da-8ae6-e7db5a9dfa7f

> Executing Control task [start] for Infrastructure/folder/host2/tc1, task id b0b42f5d-34b2-4275-bba9-6f77cfc6893c

> Executing Control task [start] for Infrastructure/folder/gdgf/host1/tc2, task id 12be7112-7d30-4000-9420-33f9db492c7e

> Executing Control task [start] for Infrastructure/folder/gdgf/host1/tc3, task id 5ccc55fe-aacd-4cf3-b43b-ef46c04e5638

> Executing Control task [start] for Infrastructure/folder/host2/tc3, task id 0c3c9b2c-d490-4235-88f4-315fa8f7e0db

> Executing Control task [start] for Infrastructure/folder/host2/tc99, task id 3337dc9c-3169-490b-b18f-2af7db944603
````

## Installation
Build the plugin and drop the JAR from build/libs/ in the \<XLD_SERVER\>/plugins folder. Restart XLD deploy.
