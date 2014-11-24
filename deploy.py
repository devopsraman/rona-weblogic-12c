import sys;

oracle_home=sys.argv[1]
readTemplate("%s/wlserver/common/templates/wls/wls.jar" % oracle_home)

wlsUsername='weblogic'
wlsPassword='welcome1'

wlsCrmUsername='wls_sai_tester'
wlsCrmPassword='Welcome1'
wlsCrmGroup='SiebelSAIUsers'

siebelCrmUsername='SADMIN'
siebelCrmPassword='SADMIN'

resourceID="type=<eis>, application=SiebelResourceAdapter, module=SiebelResourceAdapter, eis=Siebel CRM, destinationId=eis/siebel/SiebelResourceAdapterConnFactory"

startServer(jvmArgs='-XX:MaxPermSize=256m, -Xmx512m  ', username=wlsUsername, password=wlsPassword, domainDir="%s/user_projects/domains/base_domain" % oracle_home)

connect(wlsUsername, wlsPassword, 't3://127.0.0.1:7001')

deploy('SiebelResourceAdapter', '%s/siebel/SiebelResourceAdapter'  % oracle_home)

cd('/')
currentDomainName=cmo.getName()
cd('serverConfig:/SecurityConfiguration/' + currentDomainName + '/Realms/myrealm/AuthenticationProviders/DefaultAuthenticator')

cmo.createGroup(wlsCrmGroup , wlsCrmGroup)
cmo.createUser(wlsCrmUsername, wlsCrmPassword , 'user for siebel')
cmo.addMemberToGroup(wlsCrmGroup,wlsCrmUsername)

cd('serverConfig:/SecurityConfiguration/' + currentDomainName + '/Realms/myrealm/CredentialMappers/DefaultCredentialMapper')

cmo.setUserPasswordCredential(resourceID, siebelCrmUsername, siebelCrmPassword)
cmo.setUserPasswordCredentialMapping(resourceID, wlsCrmUsername, siebelCrmUsername)

cd('/')

shutdown()
exit()
