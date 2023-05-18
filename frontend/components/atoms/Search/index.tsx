import { HiOutlineSearch } from 'react-icons/hi'

type Props = {
	value: string
	onChange: (e: React.ChangeEvent<HTMLInputElement>) => void
}

const SearchInput = ({ value, onChange }: Props): JSX.Element => {
	return (
		<div className='relative'>
			<div className='flex items-center justify-start gap-1.5'>
				<div className='pointer-events-none absolute inset-y-0 left-0 flex items-center pl-2'>
					<HiOutlineSearch className='text-sm text-gray-400' />
				</div>
				<input
					type='text'
					name='search'
					className='h-9 w-64 rounded-md border border-gray-400 bg-white p-2 pl-7 text-xs placeholder-gray-400 text-sm text-gray-800 focus:outline focus:outline-blue-500'
					placeholder='Search'
					value={value}
					onChange={onChange}
				/>
			</div>
		</div>
	)
}

export default SearchInput
