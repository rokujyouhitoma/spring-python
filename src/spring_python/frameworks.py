from abc import abstractmethod
from typing import Any, Callable, Dict


class Configuration(object):
    instance = None

    def __init__(self, AppConfig: Callable) -> None:
        self.appConfig = AppConfig()
        Configuration.instance = self  # TODO


class ApplicationContext(object):
    def getBean(self, Klass: Callable) -> Any:
        pass


class AnnotationConfigApplicationContext(ApplicationContext):
    def __init__(self, configuration: Configuration) -> None:
        self.configuration = configuration

    def getBean(self, Klass: Callable) -> Any:
        name = Klass.__name__

        def getMethodName(s: str) -> str:
            return s[:1].lower() + s[1:]

        methodName = getMethodName(name)
        bean = getattr(self.configuration.appConfig, methodName)
        return bean.call(self.configuration.appConfig)


class Bean(object):
    appConfig = None

    def __init__(self, function: Callable) -> None:
        self.function = function
        self.scope = Singleton()

    def __call__(self) -> Any:
        return self.call(Configuration.instance)

    def call(self, appConfig: Any) -> Any:
        self.appConfig = appConfig
        return self.scope.getInstance(self)

    def generate(self) -> Any:
        return self.function(self.appConfig)


class Scope(object):
    @abstractmethod
    def getInstance(self, bean: Bean) -> Any:
        pass


class Prototype(Scope):
    def getInstance(self, bean: Bean) -> Any:
        return bean.generate()


class Singleton(Scope):
    beans: Dict = {}

    def getInstance(self, bean: Bean) -> Any:
        if bean in self.beans:
            return self.beans.get(bean)
        else:
            instance = bean.generate()
            self.beans.setdefault(bean, instance)
            return instance
