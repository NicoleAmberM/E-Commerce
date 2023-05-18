export interface RoleType {
  id: number
  name: string
}

export interface UserType {
  id: number
  role: RoleType
  slug: string
  first_name: string
  last_name: string
  email: string
  contactNumber: string
  address: string
}

export interface CategoryType {
  id: number
  name: string
}

export interface ProductType {
  id: number
	name: string
	slug: string
  category: string
  categorySlug: string
	price: number
	description: string
  ratings: RatingType[]
}

export interface RatingType {
  // id: number
  // product: ProductType
  // customer: UserType
  score: number
  // review: string
  // createdAt: string
}