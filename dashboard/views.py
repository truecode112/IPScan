from django.http import JsonResponse
import json
import nmap3


def scan(request):
    if (request.method == 'POST'):
        parsed_body = json.loads(request.body)
        target = parsed_body.get('target')
        tags = parsed_body.get('tags')
        label = parsed_body.get('label')

        nm = nmap3.Nmap()
        result = nm.scan_top_ports('upwork.com')
        print('======', result)

        # nm = nmap.PortScanner()
        # nm.scan(target, arguments='-p 1-1000')
        
        # for host in nm.all_hosts():
        #     print('====================================')
        #     print("Host : %s (%s)" % (host, nm[host].hostname()))
        #     print("State : %s" % nm[host].state())
        #     for proto in nm[host].all_protocols():
        #         print('----------')
        #         print("Protocol : %s" % proto)

        #         lport = nm[host][proto].keys()
        #         lport.sort()
        #         for port in lport:
        #             print("Port : %s\tstate : %s" % (port, nm[host][proto][port].state()))
        
        # Get the results
        scan_results = nm.csv().splitlines()
        print('=====', scan_results)
        return JsonResponse({'success': True,'scanResults': scan_results})
