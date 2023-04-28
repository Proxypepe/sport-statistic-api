from fastapi import APIRouter, Depends, status, Response
from dependency_injector.wiring import inject, Provide

from src.di.containers import Container


