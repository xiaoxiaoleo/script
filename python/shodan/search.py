import shodan

SHODAN_API_KEY = "x"

api = shodan.Shodan(SHODAN_API_KEY)


try:
        # Search Shodan
        results = api.search('netgear country:"AU"')

        # Show the results
        print 'Results found: %s' % results['total']
        for result in results['matches']:
                print '%s  %s' % (result['ip_str'],result['port'])
                #print result['data']
                print ''
except shodan.APIError, e:
        print 'Error: %s' % e
