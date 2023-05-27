import { BsStarFill } from 'react-icons/bs'

type Props = {
	rating: number
}

const Ratings = ({ rating }: Props): JSX.Element => {
	return (
		<div className='flex gap-0.5 text-xs text-yellow-400'>
			<BsStarFill />
			<BsStarFill />
			<BsStarFill />
			<BsStarFill />
			<BsStarFill />
		</div>
	)
}

export default Ratings
