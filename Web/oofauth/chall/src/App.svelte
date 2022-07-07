<script lang="ts">
	import { Box, Grid, Stack, Spacer } from '@kahi-ui/framework';
	import { Switch, Badge, Button, Card } from '@kahi-ui/framework';
	import { Code, Form, TextInput, Text } from '@kahi-ui/framework';
	import { updateSvg as jdentIconUpdate } from 'jdenticon';
	import { Md5 } from 'ts-md5/dist/md5';
	import { userCache } from './lib/config';
	import { createLoadObserver, xorDecode, reverse } from './lib/utils';
	import type { palette } from "./types/app.type";
	import { cache, theme } from './lib/store';

	const reversedMd5 = [
		'bf69dcbf5a8349609979c70b17411963',
		'e396152e4f3290fdd6844c33dea03184',
		'a5d1634125d4f171138d65e66b2eac6a',
		'4bb8c507c6fd03550ff6840a3430e480'
	];
	localStorage.cache = JSON.stringify(reversedMd5);
	localStorage.flag = 'TkhPLz01ElYaAB0eBBsdNwwLAxU2BQ0KGjJFDA0aCh4eQBQ=';
	localStorage.theme = 'light';

	let accountOk: boolean;
	let passOk: boolean;

	let user = '';
	let pass = '';
	let loginClicked = false;

	$: barcolor = accountOk ? (passOk ? 'affirmative' as palette: 'alert' as palette) : 'negative' as palette;

	$: findUserIdentHash = (query: string): string => {
		loginClicked = false;
		var result = userCache.find((obj) => {
			return obj.usr === query;
		});
		const temp =  result ? reverse(reversedMd5[result.identicon]?.split('')) : reverse(reversedMd5[0]?.split(''));
		return temp;
	};

	$: userExists = (query: string): boolean => {
		return findUserIdentHash(query) != reverse(reversedMd5[0].split(''));
	};

	$: identHash = findUserIdentHash(user);
	$: accountOk = userExists(user);
	$: passOk = Md5.hashStr(pass) == identHash;
	$: flag = xorDecode(pass, localStorage.flag);

	const onload = createLoadObserver(() => {
		jdentIconUpdate('#identicon', identHash);
	});
	
	const handleClick = () => {
		loginClicked = true;
	}

</script>
<Stack class="grid-spacing" orientation="horizontal" alignment_y="desktop:center" >
	<Box padding="small" width="viewport-100" height="viewport-100">
		<Grid.Container points="2">
			<Card.Container class="card-preview" palette="light">
				<Card.Figure padding="large">
					<svg use:onload id="identicon"   />
				</Card.Figure>
				<Card.Header>
					IdentiGate
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
					<Form.Control logic_id="textinput-preview">
						<Form.Label>Use your identicode</Form.Label>
						<TextInput
							type="text"
							bind:value={user}
							on:input={() => jdentIconUpdate('#identicon', identHash)}
							placeholder="Username"
						/>
						<TextInput disabled={!accountOk} type="password" bind:value={pass} placeholder="Code" />
						<Badge palette={barcolor} />
						<Form.HelpText>
							Access problems?
							<Code>noreply@nowhere.arpa</Code>
						</Form.HelpText>
					</Form.Control>
				</Card.Section>
				<Card.Footer>
					<Button palette="accent" disabled={!passOk} on:click={handleClick}>Login</Button>
				</Card.Footer>
			</Card.Container>
			<Box  >
				{#if passOk && loginClicked}		
				<Text is="strong">Welcome back {user}!</Text>
				<Text>
					{#if passOk && user.charCodeAt(0) == 0x6a}
					  {flag}
					{:else}
					  <br/>Sorry, {user} accounts have not been implemented yet.<br/>Please use your regular account.
					{/if}
				</Text>		
				{/if}
			</Box>			
		</Grid.Container>
	</Box>

</Stack>

<style>
	:global(.card-preview) {
		max-width: 35ch;
	}
</style>
