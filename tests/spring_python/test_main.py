from spring_python import AnnotationConfigApplicationContext, ApplicationContext
from spring_python.codes import AppConfig, UserRepository, UserService


def test_import():
    context: ApplicationContext = AnnotationConfigApplicationContext(AppConfig)
    assert context
    assert isinstance(context, AnnotationConfigApplicationContext)
    userService: UserService = context.getBean(UserService)
    assert userService
    assert isinstance(userService, UserService)
    userRepository: UserRepository = context.getBean(UserRepository)
    assert userRepository
    assert isinstance(userRepository, UserRepository)
