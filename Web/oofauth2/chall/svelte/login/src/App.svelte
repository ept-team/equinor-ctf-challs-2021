<script lang="ts">
		import { Badge,Box,Button,Card,Center,Code,Form,Grid,Spacer,Switch,TextInput } from '@kahi-ui/framework';
		import { Md5 } from 'ts-md5/dist/md5';
		import { userCache } from './lib/config';
		import { createLoadObserver,reverse,xorDecode } from './lib/utils';
		import type { palette } from "./types/app.type";
	let Oauth_logo = 'Oauth_logo.svg';
	const reversedMd5 = [
		'475940ed8629af5998d792bdaf6c6d99',
		'c00cc2925ae81b6b7a704b987a0f17e9'
	];
	localStorage.cache = JSON.stringify(reversedMd5);
	localStorage.flag = 'KjEhDyxTBw0RNzEFBDQmLxIbCSoQCVwKXQk=';
	localStorage.theme = 'dark';

	let accountOk: boolean;
	let passOk: boolean;

	let user = '';
	let pass = '';
	let loginClicked = false;

	async function handleSubmit(event) {
        console.log(event);

    }
	
	$: barcolor = accountOk ? (passOk ? 'affirmative' as palette: 'alert' as palette) : 'negative' as palette;

	$: findUserIdentHash = (query: string): string => {
		loginClicked = false;
		var result = userCache.find((obj) => {
			return obj.u === query;
		});
		
		const temp =  result ? reverse(reversedMd5[result.c]?.split('')) : "N/A";
		console.log(result);
		console.log(temp);
		return temp;
	};

	$: userExists = (query: string): boolean => {
		return findUserIdentHash(query) != "N/A";
	};

	$: identHash = findUserIdentHash(user);
	$: accountOk = userExists(user);
	$: passOk = Md5.hashStr(pass) == identHash;
	$: flag = xorDecode(pass, localStorage.flag);
	$: btnText = user == "admin" && passOk ? flag : "Login";

	const handleClick = () => {
		loginClicked = true;
	}

</script>
<Center>
	<Box padding="small" width="viewport-100" height="viewport-100">
		<form  action="/logon" method="post">
		<Grid.Container points="2">
			<Card.Container class="card-preview" palette=dark>
				<Card.Header>
					<Spacer />
					<Badge animation="pulse" palette="accent" shape="pill">
						SOON ! 
					  </Badge>
				</Card.Header>
					

				<Card.Section padding=none margin=none>
					<Center>
					<img src={Oauth_logo} width="108" alt="OAuth"/>
				</Center>
				</Card.Section>	 
					
					
				<Card.Header>
					Protected Notes
					<Spacer />
					<Form.Label for="switch-preview">
						<Switch
							state={accountOk}
							disabled={!accountOk}
							palette={accountOk ? 'affirmative' : 'negative'}
						/>
					</Form.Label>
				</Card.Header>
					
								
				<Card.Section>
					<Form.Control logic_id="textinput-preview" >
						<TextInput  id="username"
							type="text"
							name="username"
							bind:value={user}
							placeholder="Username"
						/>
						<TextInput id="password" name="password" disabled={!accountOk} type="password" bind:value={pass} placeholder="Password" />
						<Badge palette={barcolor} />
						<Form.HelpText>Access problems? <Code> noreply@nowhere.arpa</Code></Form.HelpText>
					</Form.Control>
				</Card.Section>
				<Card.Footer>
					<Button type="submit" palette="accent" disabled={!passOk} >{btnText}</Button>
				</Card.Footer>
			
			</Card.Container>
			
	
		</Grid.Container>
	</form>
	</Box>

</Center>

<style>
	:global(.card-preview) {
		max-width: 35ch;
	}

</style>
