FROM weblogic-12c

MAINTAINER Ronan Gill <ronan.gill@vodafone.com>

ADD deploy.py /u01/app/oracle/middleware/deploy.py
ADD siebel /u01/app/oracle/middleware/siebel

USER oracle
WORKDIR /u01/app/oracle/middleware/user_projects/domains/base_domain

RUN /u01/app/oracle/middleware/wlserver/common/bin/wlst.sh -skipWLSModuleScanning /u01/app/oracle/middleware/deploy.py /u01/app/oracle/middleware

USER root
RUN rm -f /u01/app/oracle/middleware/deploy.py
