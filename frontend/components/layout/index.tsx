import Head from 'next/head'

type Props = {
	pageTitle: string
	children: JSX.Element
}

const Layout = ({ pageTitle, children }: Props): JSX.Element => {
	return (
		<div>
			<Head>
				<title>{pageTitle}</title>
				<meta charSet='UFT-8' />
				<meta
					name='viewport'
					content='width=device-width, initial-scale=1.0'
				/>
				<meta httpEquiv='X-UA-Compatible' content='ie=edge' />
			</Head>
			<div>{children}</div>
		</div>
	)
}

export default Layout
