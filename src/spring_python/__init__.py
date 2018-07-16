from abc import abstractmethod
from typing import Any

# Framework codes


class Configuration(object):
    appConfig = None

    def __init__(self, AppConfig) -> None:
        self.appConfig = AppConfig()


class ApplicationContext(object):
    def getBean(self, Klass) -> Any:
        pass


class AnnotationConfigApplicationContext(ApplicationContext):
    configuration: Configuration = None

    def __init__(self, configuration: Configuration) -> None:
        self.configuration = configuration

    def getBean(self, Klass) -> Any:
        name = Klass.__name__

        def getMethodName(s):
            return s[:1].lower() + s[1:]

        methodName = getMethodName(name)
        # TODO: xxx
        bean = getattr(self.configuration.appConfig, methodName)
        return bean.call(self.configuration.appConfig)


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
    def __init__(self):
        pass

    def register(self, user: User, rawPassword: str) -> None:
        pass


class UserServiceImpl(UserService):
    def __init__(self, userRepository: UserRepository,
                 passwordEncoder: PasswordEncoder):
        self.userRepository = userRepository
        self.passwordEncoder = passwordEncoder

    def save(self, user: User) -> None:
        return

    def countByUserName(self, userName: str) -> int:
        return 0


class BCryptPasswordEncoder(PasswordEncoder):
    def encode(self, rawPassword: str) -> str:
        return ''


class Bean(object):
    method = None

    def __init__(self, function):
        self.function = function

    def call(self, appConfig):
        return self.function(appConfig)

    def __call__(self):
        # TODO: Is it OK? > {}
        return self.function({})


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
