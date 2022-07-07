
<script lang="ts">
	import { Anchor,Box,Button,Center,Check,Code,Divider,Form,Heading,Spacer,Stack,Table,Text } from '@kahi-ui/framework';
let Oauth_logo = 'Oauth_logo.svg';
	let logic_state = ["1","2","4","5","6","7"];
	let noaccess =  "{ error: unauthorized }";
</script>

	<Box padding="small" width="viewport-100" height="viewport-100">
		<Stack orientation="horizontal">
			<Spacer />
			<Button variation="outline" href="/logout">Logout</Button>
		</Stack>		
		<Center><Heading>My TODO's</Heading></Center>
		<Form.Group bind:logic_state>
		<Table.Container  variation={["borders", "stripes"]}>
			<Table.Header>
				<Table.Row>
					<Table.Heading>TODO</Table.Heading>
					<Table.Heading>DESCRIPTION</Table.Heading>
					<Table.Heading>DONE</Table.Heading>
				</Table.Row>
			</Table.Header>
		
			<Table.Section>
				<Table.Row>
					<Table.Column><Text is="strong" >01. Rewrite login system.</Text></Table.Column>
					<Table.Column><Text >Decision: OAuth2 Authorization Code Grant w/PKCS to delegate authorizations</Text></Table.Column>
					<Table.Column><Check palette="accent" size="tiny" value="0" ></Check></Table.Column>
				</Table.Row>
				
				<Table.Row>
					<Table.Column>
						<Text is="strong" palette="affirmative">02. Read up and do my own research</Text>
					</Table.Column>
					<Table.Column>
						<Text class="strikeout">
							<Anchor	href="https://datatracker.ietf.org/doc/html/rfc6749#section-4.1" target="_blank" rel="noopener noreferrer">RFC 6749 ch. 4.1</Anchor>							
							 Authorization Code Grant</Text>						
					</Table.Column>					
					<Table.Column><Check palette="accent" size="tiny" value="1" disabled></Check></Table.Column>
				</Table.Row>

				<Table.Row>
					<Table.Column>
						<Text is="strong" palette="affirmative">03. Read up on PKCE for added security</Text>
					</Table.Column>
					<Table.Column>
						<Text class="strikeout">
							<Anchor	href="https://datatracker.ietf.org/doc/html/rfc7636" target="_blank" rel="noopener noreferrer">RFC 7636</Anchor>
							PKCE code challenge</Text>						
					</Table.Column>					
					<Table.Column><Check palette="accent" size="tiny" value="2" disabled></Check></Table.Column>
				</Table.Row>
				<Table.Row>
					<Table.Column><Text is="strong">04. Store secrets</Text></Table.Column>
					<Table.Column><Text>Just paste this here for now... store them somewhere safer later</Text><Text>client_id: <Code>backend</Code>, client_secret: <Code>drowssapgnoldesrever</Code></Text></Table.Column>
					<Table.Column><Check id="check-2"	palette="accent" size="tiny" value="3"></Check></Table.Column>
				</Table.Row>		
				<Table.Row>
					<Table.Column><Text is="strong">05. Possible scopes</Text></Table.Column>
					<Table.Column><Text></Text><Text>scope: <Code>read</Code>, <Code>read.protected</Code>, <Code>protected.read</Code></Text></Table.Column>
					<Table.Column><Check id="check-2"	palette="accent" size="tiny" value="4"></Check></Table.Column>
				</Table.Row>							
				<Table.Row>
					<Table.Column><Text  is="strong" palette="affirmative">06. Implement Authorization Request endpoint (section-4.1.1)</Text></Table.Column>
					<Table.Column><Text class="strikeout">/authorize</Text></Table.Column>
					<Table.Column><Check palette="accent" size="tiny" value="5" disabled></Check></Table.Column>
				</Table.Row>
				<Table.Row>
					<Table.Column><Text  is="strong" palette="affirmative">07. Implement Authorization Response callback endpoint (section-4.1.2)</Text></Table.Column>
					<Table.Column><Text class="strikeout">/callback</Text></Table.Column>
					<Table.Column><Check palette="accent" size="tiny" value="6" disabled></Check></Table.Column>
				</Table.Row>					
				<Table.Row>
					<Table.Column><Text  is="strong" palette="affirmative">08. Implement Access Token Request endpoint (section-4.1.3)</Text></Table.Column>
					<Table.Column><Text class="strikeout">/token</Text></Table.Column>
					<Table.Column><Check palette="accent" size="tiny" value="7" disabled></Check></Table.Column>
				</Table.Row>				
				<Table.Row>
					<Table.Column><Text is="strong" palette="affirmative">09. Implement endpoint for Accessing Protected Resources (section-7)</Text></Table.Column>
					<Table.Column><Text class="strikeout">/protected</Text></Table.Column>
					<Table.Column><Check palette="accent" size="tiny" value="8" disabled></Check></Table.Column>
				</Table.Row>				
				<Table.Row>
					<Table.Column><Text  is="strong" palette="affirmative">10. Move all my sensitive data</Text></Table.Column>
					<Table.Column><Text class="strikeout">Move important data behind my protected endpoint</Text></Table.Column>
					<Table.Column><Check palette="accent" size="tiny" value="9" disabled></Check></Table.Column>
				</Table.Row>							
				<Table.Row>
					<Table.Column><Text  is="strong">11. Connect everything together</Text></Table.Column>
					<Table.Column><Text>Finish up and connect everything in the oauth dance so everything is working nicely together</Text></Table.Column>
					<Table.Column><Check palette="accent" size="tiny" value="10"></Check></Table.Column>
				</Table.Row>		
				<Table.Row>
					<Table.Column><Text  is="strong">12. Write tests</Text></Table.Column>
					<Table.Column><Text>Next time write them before I begin to code...</Text></Table.Column>
					<Table.Column><Check palette="accent" size="tiny" value="11"></Check></Table.Column>
				</Table.Row>		
				<Table.Row>
					<Table.Column><Text is="strong" >13. Take a vacation</Text></Table.Column>
					<Table.Column><Text>🚢 ...</Text></Table.Column>
					<Table.Column><Check palette="accent" size="tiny" value="12"></Check></Table.Column>
				</Table.Row>	

			</Table.Section>
				
		</Table.Container>
		<Divider />		
	 <Heading align="center">Protected Notes</Heading>
	 <br/>
		<Center><Code palette="negative">{ noaccess }</Code></Center>
		</Form.Group>
	</Box>


<style>
	:global(.card-preview) {
		max-width: 35ch;
	}
	:global(.strikeout) {
		text-decoration:line-through;
	}
</style>
