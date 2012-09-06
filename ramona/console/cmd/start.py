import json
from ... import cnscom
###

name = 'start'
cmdhelp = 'Launch subprocess(es)'

###

def init_parser(parser):
	parser.add_argument('-n','--no-server-start', action='store_true', help='Avoid eventual automatic server start')
	parser.add_argument('-f','--force-start', action='store_true', help='Force start of processes in FATAL state')
	parser.add_argument('-S','--server-only', action='store_true', help='Start only server, programs are not launched')
	parser.add_argument('program', nargs='*', help='Optionally specify program(s) in scope of the command')

###

def main(cnsapp, args):
	if args.server_only:
		if len(args.program) > 0:
			raise exception.parameters_error('Cannot specify programs and -S option at once.')
		cnsapp.auto_server_start()
		return

	params={'force':args.force_start}
	if len(args.program) > 0: params['pfilter'] = args.program
	cnsapp.svrcall(
		cnscom.callid_start,
		json.dumps(params),
		auto_connect=args.no_server_start,
		auto_server_start=not args.no_server_start
	)

