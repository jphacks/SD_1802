class UserInfo < ApplicationRecord
  belongs_to :user, optional: true
  mount_uploader :file, ImageUploader
end
