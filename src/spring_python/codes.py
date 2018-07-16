from abc import abstractmethod

from spring_python import Bean, Configuration

# User codes


class User(object):
    pass


class UserRepository(object):
    @abstractmethod
    def register(self, user: User, rawPassword: str) -> None:
        pass


class PasswordEncoder(object):
    @abstractmethod
    def encode(self, rawPassword: str) -> str:
        pass


class UserService(object):
    @abstractmethod
    def save(self, user: User) -> None:
        pass

    @abstractmethod
    def countByUserName(self, userName: str) -> int:
        pass


class UserRepositoryImpl(UserRepository):
    def __init__(self) -> None:
        pass

    def register(self, user: User, rawPassword: str) -> None:
        pass


class UserServiceImpl(UserService):
    def __init__(self, userRepository: UserRepository,
                 passwordEncoder: PasswordEncoder) -> None:
        self.userRepository = userRepository
        self.passwordEncoder = passwordEncoder

    def save(self, user: User) -> None:
        return

    def countByUserName(self, userName: str) -> int:
        return 0


class BCryptPasswordEncoder(PasswordEncoder):
    def encode(self, rawPassword: str) -> str:
        return ''


@Configuration
class AppConfig(object):
    @Bean
    def userRepository(self) -> UserRepository:
        return UserRepositoryImpl()

    @Bean
    def passwordEncoder(self) -> PasswordEncoder:
        return BCryptPasswordEncoder()

    @Bean
    def userService(self) -> UserService:
        return UserServiceImpl(self.userRepository(), self.passwordEncoder())
