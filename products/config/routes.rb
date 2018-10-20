Rails.application.routes.draw do
  get    'profile', to: 'user_infos#new'
  post   'profile', to: 'user_infos#create'
  
  get    'login',  to: 'sessions#new'
  post   'login',  to: 'sessions#create'
  delete 'logout', to: 'sessions#destroy'
  get    'users',  to: 'users#new'
  post   'users',  to: 'users#create'

  get    'profile_show', to: 'user_infos#show'
  
  post   'bin',    to: 'hello.php'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
