Rails.application.routes.draw do
  get    'login',  to: 'sessions#new'
  post   'login',  to: 'sessions#create'
  delete 'logout', to: 'sessions#destroy'
  get    'users',  to: 'users#new'
  post   'users',  to: 'users#create'
  post   'bin',    to: 'hello.php'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
