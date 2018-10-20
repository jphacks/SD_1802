class User < ApplicationRecord
  has_secure_password validations: true

  validates :mail, presence: true, uniqueness: true

  has_one :user_info
  
  def self.new_remember_token
    SecureRandom.urlsafe_base64
  end

  def self.encrypt(token)
    Digest::SHA256.hexdigest(token.to_s)
  end
end
